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
    return redirect(url_for('login'))


@app.route('/api/species_data')
def species_data():
    conn = mysql_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM species")
            result = cursor.fetchall()
            return jsonify(result)
    except pymysql.MySQLError() as err:
        APP_LOG.error(err)

    finally:
        conn.close()
