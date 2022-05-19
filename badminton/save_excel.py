from __const import *
from luck import excel

cells_list = load_pkl('./Data/cells.pkl')
price_list = load_pkl('./Data/price.pkl')
if __name__ == '__main__':
    title = [
        'grade', 'name', 'description', 'brand', 'species', 'other', 'link',
        'price', 'second_price', 'buy_people_num'
    ]
    temp_list = [list(cell) for cell in cells_list]
    price_list = [list(price) for price in price_list]
    res_list = [cell + price for cell, price in zip(temp_list, price_list)]
    res_list.insert(0, title)
    print(res_list)
    excel.write_xlsx('./result.xlsx', res_list)
    print('done')
