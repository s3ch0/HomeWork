from collections import namedtuple
import pickle
from selenium import webdriver
from typing import *

THE_ENTRY_POINT = "https://www.badmintoncn.com/cbo_eq/list.php?name=&class=0&brand=0"
THE_PAGE_URL_TEMPLATE = "https://www.badmintoncn.com/cbo_eq/list.php?brand=0&sort=0&class=0&fee=&name=&order=last&page={}"
THE_PRICE_URL_TEMPLATE = "https://www.badmintoncn.com/cbo_eq/view_buy.php?eid={}"
THE_DETAIL_URL_TEMPLATE = "https://www.badmintoncn.com/cbo_eq/view_specs_{}.html"

CONST_XPATH_VALUE = {
    'MAIN_TOPBAR_LINK':
    "//div[@class='list2']/table/tbody/tr/td/a", # the badminton species link
    'PAGE_CELL':
    "//div[@class='main']/div[@class='dleft']/div[@class='list']/table/tbody/tr",
    'CELL_LINK': "//div[@class='dleft']/div/table/tbody/tr/td/a[1]",
    'CELL_DETAIL_LINK': "//ul[@class='view_menu']/li/a",
    'PAGES': "//div[@class='p_bar']/a[@class='p_pages']",
    'DETAIL_STAR': "//div[@class='div_5']/table/tbody/tr/td/a",
    'DETAIL_PRICE': "//div[@class='div_5']/table/tbody/tr/td",
    'DETAIL_ALL': "//div[@class='list']/table/tbody/tr"
}
# 评分，姓名，描述，品牌，类型，fuck,链接
Cell = namedtuple(
    'Cell',
    ['grade', 'name', 'description', 'brand', 'species', 'other', 'link'])

# 参数，图库，比较，开箱测评，使用球星，评价，入手价，那儿买
Price = namedtuple('Price', ['price', 'second_price', 'buy_people_num'])

Racket = namedtuple(
    'Racket',
    ['name', 'grade', 'description', 'brand', 'species', 'other', 'link'])


def load_pkl(pkl_file_path: str) -> List[Union[Cell, Price]]:
    if isinstance(pkl_file_path, str):
        fd = open(pkl_file_path, 'rb')
        obj_list = pickle.load(fd)
        fd.close()
        return obj_list
    else:
        exit(1)


def init_chrome() -> webdriver.Chrome:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--silent')
    driver = webdriver.Chrome(chrome_options=options)
    return driver
