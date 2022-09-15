import pymysql
from flask import Flask,redirect
from flask_cors import CORS
import utils
from affiliation import log

main_log = log.Log()


if __name__ == '__main__':
    a = gen_sumscore_count()
    print(a)