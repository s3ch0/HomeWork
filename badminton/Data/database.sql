create badminton database;
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


