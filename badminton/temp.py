from __const import *

detail_info_list = load_pkl("./Data/detail.pkl")
head = [
    '装备类型', '装备品牌', '装备系列', '装备描述', '上市日期', '装备介绍', '拍框材质', '拍杆材质', '拍身重量',
    '拍身长度', '拍柄粗细', '中管韧度', '拉线磅数', '平衡点', '链接'
]

for i in detail_info_list:
    print(i[head[8]], "link", i[head[-1]])
