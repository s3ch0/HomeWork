'''
This file will crawl the badminton detail infomation to detail.pkl
INFO: the infomation use defaultdict to store the infomation
'''

from __const import *
import pickle
from selenium.webdriver.common.by import By
from rich.progress import track
from collections import defaultdict
from luck.__log import Log

HANDLE_DETAIL_LOG = Log()
cells_list = load_pkl('./Data/cells.pkl')
price_list = load_pkl('./Data/price.pkl')

if __name__ == '__main__':
    # set webdriver options
    driver = init_chrome()
    rocket = [i for i in cells_list if i.species == "羽毛球拍"]
    res_dict = defaultdict()

    for i in track(range(len(rocket)), description="Processing..."):
        index = rocket[i].link.split('/')[-1].split('.')[0].split('_')[-1]
        driver.get(THE_DETAIL_URL_TEMPLATE.format(index))
        print(THE_DETAIL_URL_TEMPLATE.format(index))
        elements_list = driver.find_elements(
            By.XPATH, CONST_XPATH_VALUE.get("DETAIL_ALL"))
        for element in elements_list:
            if element.text.strip() == "":
                continue
            tmp_items = element.text.split(' ')
            if len(tmp_items) != 2:
                if tmp_items[0] == '平':
                    key = "".join(tmp_items[0:3])
                    value = tmp_items[3:]
                else:
                    key = tmp_items[0]
                    value = tmp_items[1::]
            else:
                key = tmp_items[0]
                value = tmp_items[1]

            res_dict[str(key)] = "".join(value).strip()
        HANDLE_DETAIL_LOG.info(str(res_dict))

    # save to pickle
    with open('./Data/detail.pkl', 'wb') as f:
        pickle.dump(res_dict, f)
    driver.quit()
    HANDLE_DETAIL_LOG.process(
        "Successfully handle {} detail infomation".format(len(res_dict)))
    HANDLE_DETAIL_LOG.complete("handle detail success")
