-- Delete the badminton database if exists
--

DROP database badminton;

CREATE DATABASE badminton DEFAULT CHARSET UTF8MB4;
use badminton;


create table cell
(
grade decimal(4,1) comment '评分',
name varchar(100) not null comment '名称',
description TEXT comment '描述',
brand varchar(100) comment '品牌',
species varchar(100) comment '种类',
other varchar(100) comment '其他',
link varchar(150) comment '链接',
price decimal(10,1) comment '价格'
);


create table detail
(
type varchar(100) comment '类型',
species varchar(100) comment '品牌',
series varchar(100) comment '系列',
description TEXT comment '描述',
time int comment '上市日期',
introduce TEXT comment '装备介绍',
frame_material varchar(100) comment '拍框材质',
shaft_material varchar(100) comment '拍杆材质',
max_shaft_weight decimal(10,1) comment '最大拍质量',
min_shaft_weight decimal(10,1) comment '最小拍质量',
shaft_length decimal(10,1) comment '拍杆长度',
handle_thick varchar(100) comment '拍柄粗细',
tube_toughness varchar(100) comment '中管韧度',
max_pounds decimal(10,1) comment '最大磅数',
min_pounds decimal(10,1) comment '最小磅数',
balance varchar(100) comment '平衡点',
link varchar(150) comment '球拍链接'
);


