"""
This file will crawl the badminton detail infomation to detail.pkl
INFO: the infomation use defaultdict to store the infomation
"""
from selenium.webdriver.chrome.webdriver import WebDriver
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

    HANDLE_DETAIL_LOG.info("Start crawling...")
    driver: WebDriver = init_chrome()
    rocket = [i for i in cells_list if i.species == "羽毛球拍"]
    res_dict = defaultdict()
    url = [cell.link for cell in rocket]
    res_list = []

    HANDLE_DETAIL_LOG.info('will start crawl {} infomation'.format(len(url)))
    # 3632
    for i in track(range(len(url)), description="Processing..."):
        # init the dict
        res_dict = defaultdict()
        index = rocket[i].link.split('/')[-1].split('.')[0].split('_')[-1]
        driver.get(THE_DETAIL_URL_TEMPLATE.format(index))
        HANDLE_DETAIL_LOG.process(f'Processing {i}')
        HANDLE_DETAIL_LOG.info("The link is: {}".format(
            THE_DETAIL_URL_TEMPLATE.format(index)))

        elements_list = driver.find_elements(
            By.XPATH, CONST_XPATH_VALUE.get("DETAIL_ALL"))

        # process the temp data
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

        res_list.append(res_dict)
        #  HANDLE_DETAIL_LOG.info(f"{res_dict.keys()}")
        # print the length of the dict
        HANDLE_DETAIL_LOG.info(f"The length of the dict: {len(res_dict)}")

    # save to pickle
    pickle_path = './Data/detail_05.pkl'
    with open(pickle_path, 'wb') as f:
        pickle.dump(res_list, f)
    driver.quit()
    HANDLE_DETAIL_LOG.process(
        "Successfully handle {} detail infomation".format(len(res_list)))
    HANDLE_DETAIL_LOG.complete("handle {} success".format(pickle_path))
