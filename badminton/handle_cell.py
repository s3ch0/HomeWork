from selenium import webdriver
import pickle
from selenium.webdriver.common.by import By
from collections import namedtuple
from __const import *
from rich.progress import track
from luck.__base import is_number
from luck.excel import *

HANDLE_LOG = Log()

cells = []
detail = []


def element_to_dict(the_element_list: ...) -> dict:
    res_dict = {}
    for _ in the_element_list:
        temp = {_.text: _.get_attribute("href")}
        res_dict.update(temp)
    return res_dict


# TODO Complete the cell process
def cell_process(cell_string: str, the_link) -> Cell:
    cell_list = cell_string.split("\n")
    # This statement is use to check the grade is empty or not and the description is empty or not
    # In my opinion, this code is so junk and ugly
    if not is_number(cell_list[0]):
        cell_list.insert(0, 'None')
    if is_number(cell_list[0]) and eval(cell_list[0]) > 10:
        cell_list.insert(0, 'None')
    if len(cell_list) == 5:
        cell_list.insert(2, 'None：None')
    # ----------------
    for i in range(2, 5):
        cell_list[i] = cell_list[i].split("：")[1]
    my_cell = Cell(*cell_list, the_link)
    return my_cell


if __name__ == '__main__':
    cells_list = []
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    # hide the browser
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    url = THE_ENTRY_POINT
    chrome = webdriver.Chrome(chrome_options=chrome_options)
    # use the option to set the headless mode
    chrome.get(url)
    chrome.implicitly_wait(10)
    HANDLE_LOG.process("Start to handle the entry point page")
    pages = chrome.find_element(By.XPATH, value=CONST_XPATH_VALUE["PAGES"])
    max_page_num = int(pages.text.split('/')[1])
    the_page_url = THE_PAGE_URL_TEMPLATE

    # use progress to show the progress

    for page_num in track(range(max_page_num + 1),
                          description="Processing..."):
        page_url = the_page_url.format(page_num)
        chrome.get(page_url)
        # wait
        chrome.implicitly_wait(10)
        cells = chrome.find_elements(By.XPATH,
                                     value=CONST_XPATH_VALUE["PAGE_CELL"])
        cells_link = chrome.find_elements(By.XPATH,
                                          value=CONST_XPATH_VALUE["CELL_LINK"])
        cells_link_list = [i.get_attribute('href') for i in cells_link]
        cells_string_list = [_.text for _ in cells]
        cells_container = [
            cell_process(cell, link)
            for cell, link in zip(cells_string_list, cells_link_list)
        ]
        cells_list.extend(cells_container)

    chrome.quit()
    cells_data_file = open("cells.pkl", "wb")
    pickle.dump(cells_list, cells_data_file)
    cells_data_file.close()
    HANDLE_LOG.complete("Finish the handle")
