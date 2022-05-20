import pymysql
from luck.__log import Log
from flask import Flask, redirect, url_for, jsonify
from flask_cors import CORS
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
        cursor.execute(
            "select species,count(*) as num from cell group by species;")
    tmp = cursor.fetchall()
    species_data_dict = {i[0]: i[1] for i in tmp}
    return {
        'species': list(species_data_dict.keys()),
        'numbers': list(species_data_dict.values())
    }


if __name__ == '__main__':
    app.run(debug=True)
