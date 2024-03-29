import os
from functools import partial
import pymysql

DB_HOST = os.environ.get('DB_HOST') or 'localhost'
DB_PORT = os.environ.get('DB_PORT') or 3306
DB_USER = os.environ.get('DB_USER') or 'root'
DB_PASS = os.environ.get('DB_PASS') or '123.com'
DB_NAME = os.environ.get('DB_NAME') or 'badminton'
DB_CHAR = os.environ.get('DB_CHAR') or 'utf8mb4'
db_config = {
    'host': "127.0.0.1",
    'port': DB_PORT,
    'user': DB_USER,
    'password': DB_PASS,
    'db': DB_NAME,
    'charset': DB_CHAR
}

connect_mysql = partial(pymysql.connect, **db_config)


def mysql_connection(database=DB_NAME):
    return connect_mysql(database=database)
