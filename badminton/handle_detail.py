'''
This file will crawl the badminton detail infomation to detail.pkl

'''

from __const import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from rich.progress import track

cells_list = load_pkl('./Data/cells.pkl')
price_list = load_pkl('./Data/price.pkl')

if __name__ == '__main__':
    # set webdriver options
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=options)
    rocket = [i for i in cells_list if i.species == "羽毛球拍"]

    for i in track(range(len(rocket)), description="Processing..."):
        index = rocket[i].link.split('/')[-1].split('.')[0].split('_')[-1]
        driver.get(THE_DETAIL_URL_TEMPLATE.format(index))
