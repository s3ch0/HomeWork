import pickle
from collections import namedtuple


def broken_atoi(text: str) ->...:
    if text == "暂无":
        return None
    res = ''
    for i in text:
        if i.isdigit():
            res += i
        else:
            break
    return int(res)


Cell = namedtuple(
    'Cell',
    ['grade', 'name', 'description', 'brand', 'species', 'other', 'link'])
Price = namedtuple('Price', ['price', 'second_price', 'buy_people_num'])
# read cells.pkl
cells_data = open("cells.pkl", 'rb')
cells_list = pickle.load(cells_data)
cells_data.close()

price_data = open("price.pkl", 'rb')
price_list = pickle.load(price_data)
price_data.close()
print(price_list)

temp_sql = "insert into cell value({}, '{}', '{}', '{}', '{}', '{}', '{}', {})"
sql_file = open("cell.sql", 'w')

for cell, price in zip(cells_list, price_list):
    sql_file.write(
        temp_sql.format(cell.grade, cell.name, cell.description, cell.brand,
                        cell.species, cell.other, cell.link,
                        broken_atoi(price.price)))
    sql_file.write('\n')
sql_file.close()
