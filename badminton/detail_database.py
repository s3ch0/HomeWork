import re

from __const import *

# -------------------------------------------------------------------|
# this file is used to process the data and store it in the database |
# but the function is templated                                      |
# and the function is so bad that I can't write it in a good way     |
# for example, the function process_weight,process_length...         |
# -------------------------------------------------------------------|

_the_template_dict = {
    "2U": [90, 94],
    "3U": [85, 89],
    "4U5": [80, 84],
    "4U4": [80, 84],
    "4U": [80, 84],
    "5U": [75, 79],
    "6U": [70, 74],
    "7U": [65, 69],
    "8U": [60, 64],
    "W2": [90, 94],
    "W3": [85, 89],
    "W4": [80, 84],
    "W5": [75, 79],
    "W6": [70, 74],
    "W7": [65, 69],
    "G2": ["", ""],
    "G3": ["", ""],
    "G4,5": ["", ""],
    "G4": ["", ""],
    "G5": ["", ""],
    "G6": ["", ""],
    "S2": ["", ""],
    "2L": ["", ""]
}

# this function is used to process the temp num
# for example:
# [22,34] -> max(),min()
# [22,30,24] -> max(),min()
# [22,4] -> max()+min(),max-min()


def _process_num(num_list: list, condition: int) -> tuple:
    if len(num_list) == 0:
        return 0, 0
    elif len(num_list) == 1:
        if (float(num_list[0]) <= condition):
            return 0, 0
        else:
            return float(num_list[0]), float(num_list[0])
    elif len(num_list) == 2:
        if float(min(num_list)) <= condition:
            return float(max(num_list)) + float(min(num_list)), float(
                max(num_list)) - float(min(num_list))
        else:
            return float(max(num_list)), float(min(num_list))
    else:
        if float(min(num_list)) <= condition:
            return float(max(num_list)) + float(min(num_list)), float(
                max(num_list)) - float(min(num_list))

        return float(max(num_list)), float(min(num_list))


def process_date(date_raw_str: str) -> Union[None, int]:
    # gain num
    date_raw_str = date_raw_str.replace(".", "-")
    num_list = re.findall(r"\d+\.?\d*", date_raw_str)

    if len(num_list) == 0:
        return None
    else:
        if float(max(num_list)) > 1000:
            return int(max(num_list))
        else:
            return None


def process_weight(weight_raw_str: str) -> tuple:
    temp = weight_raw_str.upper()
    for k, v in _the_template_dict.items():
        temp = temp.replace(k, str(v[0]) + " " + str(v[1]) + " ")
    # extract the number in the temp
    num_list = re.findall(r"\d+\.?\d*", temp)
    return _process_num(num_list, 20)


def process_length(length_raw_str: str) -> float:
    # gain num
    num_list = re.findall(r"\d+\.?\d*", length_raw_str)
    if len(num_list) == 0:
        return 0
    else:
        if float(num_list[0]) <= 10:
            return float(num_list[0]) + 664
        elif 20 <= float(num_list[0]) <= 30:
            return float(num_list[0]) * 10
        elif 50 < float(num_list[0]) < 70:
            return float(num_list[0]) * 10
        elif 100 > float(num_list[0]) > 70:
            return 0
        else:
            return float(num_list[0])


def process_stiff(stiff_raw_str: str) -> tuple:
    # gain num
    num_list = re.findall(r"\d+\.?\d*", stiff_raw_str)
    return _process_num(num_list, 8)

    #  return _process_num(num_list, 10)


head = [
    '装备类型', '装备品牌', '装备系列', '装备描述', '上市日期', '装备介绍', '拍框材质', '拍杆材质', '拍身重量',
    '拍身长度', '拍柄粗细', '中管韧度', '拉线磅数', '平衡点', '链接'
]

if __name__ == '__main__':
    main_list = load_pkl("./Data/detail.pkl")
    the_index = 0
    max_weight = 0
    min_weight = 0
    temp_res = []
    # save to sql file
    # process main_list

    for index, key in enumerate(main_list):
        temp_res = []
        temp_res.append(key[head[0]])
        temp_res.append(key[head[1]])
        temp_res.append(key[head[2]])
        temp_res.append(key[head[3]])
        date_time = process_date(key[head[4]])
        if date_time > 3000:
            temp_res.append(None)
        temp_res.append(date_time)
        temp_res.append(key[head[5]])
        temp_res.append(key[head[6]])
        temp_res.append(key[head[7]])
        weight = process_weight(key[head[8]])
        temp_res.append(weight[0])
        temp_res.append(weight[1])
        length = process_length(key[head[9]])
        if length >= 1000:
            temp_res.append(0)
        else:
            temp_res.append(length)
        temp_res.append(key[head[10]])
        temp_res.append(key[head[11]])
        stiff = process_stiff(key[head[12]])
        temp_res.append(stiff[0])
        temp_res.append(stiff[1])
        temp_res.append(key[head[13]])
        temp_res.append(key[head[14]])
        temp_str = str(temp_res)[1:-1]
        insert_sql = f"insert into detail values({temp_str});"
        with open("./Data/detail.sql", "a") as f:
            f.write(insert_sql + "\n")
