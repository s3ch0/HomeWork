import pymysql
from __sqlconst import *
from luck.__log import Log
from flask import Flask, redirect, url_for, jsonify
from flask_cors import CORS
from collections import defaultdict
from utils import *
import setting


APP_LOG = Log()
app = Flask(__name__)
app.config.from_object(setting)
CORS(app, supports_credentials=True)


@app.route('/')
def index():
    return redirect('./static/index.html')


@app.route('/api/species_data')
def species_data():
    conn = mysql_connection()
    with conn.cursor() as cursor:
        cursor.execute(SQL_CMD.get('species_data'))
        tmp = cursor.fetchall()
        species_data_dict = {i[0]: i[1] for i in tmp}
        return {
            'species': list(species_data_dict.keys()),
            'numbers': list(species_data_dict.values())
        }


@app.route('/api/grade_data')
def grade_data():
    conn = mysql_connection()
    with conn.cursor() as cursor:
        cursor.execute(SQL_CMD.get('grade_data'))
        tmp = cursor.fetchall()
        grade_data_dict = {i[0]: i[1] for i in tmp}

        res_dict = {}

        # let 7.1,7.2 combine to 7 and sum the number
        for k, v in grade_data_dict.items():
            if k is None:
                pass
            else:
                if int(k) in res_dict.keys():
                    res_dict[int(k)] += int(v)
                else:
                    res_dict[int(k)] = 0

        grade_list = [{
            'value': v,
            'name': k
        } for k, v in res_dict.items()]

        return {'data_pie': grade_list}


@app.route('/api/species_data_')
def species_data_():
    conn = mysql_connection()
    with conn.cursor() as cursor:
        cursor.execute(SQL_CMD.get('species_data_'))
        tmp = cursor.fetchall()
        grade_data_dict = {i[0]: i[1] for i in tmp}
        grade_list = [{
            'value': v,
            'name': k
        } for k, v in grade_data_dict.items()]

        return {'data_pie': grade_list}


@app.route('/api/tough_data')
def tough_data():
    conn = mysql_connection()
    with conn.cursor() as cursor:
        cursor.execute(SQL_CMD.get('tough_data_'))
        tmp = cursor.fetchall()
        grade_data_dict = {i[0]: i[1] for i in tmp}
        res_dict = grade_data_dict
        # res_dict = {k: v for k, v in grade_data_dict if k != '-'}
        return {'y_value': list(res_dict.keys()), 'x_value': list(res_dict.values())}


@app.route('/api/time_data')
def time_data():
    conn = mysql_connection()
    with conn.cursor() as cursor:
        cursor.execute(SQL_CMD.get('time_data_'))
        tmp = cursor.fetchall()
        species_data_dict = {i[0]: i[1] for i in tmp}

        return {
            'time': list(species_data_dict.keys()),
            'numbers': list(species_data_dict.values())
        }


if __name__ == '__main__':
    app.run(debug=True)
