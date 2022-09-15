import pymysql
from flask import Flask,redirect
from flask_cors import CORS
import utils
from affiliation import log
from affiliation import embellish
main_log = log.Log()


app = Flask(__name__)
CORS(app)

def condition_select(tmp_result:dict,user_str=None):
    if user_str is not None:
        user_str=user_str+'_'
    else:
        user_str=''
    zero = 0
    not_good = 0
    simple = 0
    common = 0
    common_2=0
    good=0
    good_2=0
    very_good=0
    very_good_2=0
    best=0
    for i in list(tmp_result.keys()):

        if i ==0:
            zero +=tmp_result[i]
        if 0<i<=50:
            simple+=tmp_result[i]
        elif 50<i<60:
            not_good +=tmp_result[i]
        elif 60<=i<65:
            common += tmp_result[i]
        elif 65<=i<70:
            common_2 +=tmp_result[i]
        elif 70<=i<75:
            good+=tmp_result[i]
        elif 75<=i<80:
            good_2+=tmp_result[i]
        elif 80<=i<85:
            very_good+=tmp_result[i]
        elif 85<=i<90:
            very_good_2+=tmp_result[i]
        elif 90<=i:
            best+=tmp_result[i]
    result = {'0分/未体测':zero,"0-50":simple,'50-60':not_good,'60-65':common,"65-70":common_2,'70-75':good,"75-80":good_2,'80-85':very_good,"85-90":very_good_2,'90--':best}
    x_data = list(result.keys())
    y_data = list(result.values())
    return {user_str+'x':x_data,user_str+'y':y_data}



@app.route('/')
def show_index():
    return redirect('/static/index.html')

@app.route('/api/stuscore')
def gen_stuscore_data():
    conn = utils.get_mysql_connection()
    try:
        with conn.cursor() as cursor:
            result_flag = cursor.execute("select stuname,stu_sumscore from tb_physical_test where stu_sumscore <> '免试' and stuweight is not null")
            main_res_poor = cursor.fetchall()
            x_data = [data[0] for data in main_res_poor]
            y_data = [data[1] for data in main_res_poor]


    except pymysql.MySQLError() as err:
        main_log.error()
        main_log.error(err)
    finally:
        conn.close()

    return {'x_data':x_data,'y_data':y_data}
# 成绩分组
@app.route('/api/sumscore_count')
def gen_sumscore_count():
    conn = utils.get_mysql_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("select count(*) ,stu_sumscore from tb_physical_test group by stu_sumscore;")
            main_res_poor = cursor.fetchall()
            x_data = [data[0] for data in main_res_poor]
            y_data = [data[1] for data in main_res_poor]
    except pymysql.MySQLError() as err:
        main_log.error()
        main_log.error(err)
    finally:
        conn.close()
    tmp_result = dict(zip(y_data,x_data))
    result = condition_select(tmp_result)
    return result
# 性别成绩分组
@app.route('/api/sex_score_count')
def genSexScoreCount():
    conn = utils.get_mysql_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("select count(*) ,stu_sumscore from tb_physical_test where stusex = '男' group by stu_sumscore;")
            man_res_poor = cursor.fetchall()
            man_x_data = [data[0] for data in man_res_poor]
            man_y_data = [data[1] for data in man_res_poor]
            cursor.execute("select count(*) ,stu_sumscore from tb_physical_test where stusex = '女' group by stu_sumscore;")
            girl_res_poor = cursor.fetchall()
            girl_x_data = [data[0] for data in girl_res_poor]
            girl_y_data = [data[1] for data in girl_res_poor]

    except pymysql.MySQLError() as err:
        main_log.error()
        main_log.error(err)
    finally:
        conn.close()
    man_result = dict(zip(man_y_data,man_x_data))
    man_dict = condition_select(man_result,'man')
    girl_result = dict(zip(girl_y_data,girl_x_data))
    girl_dict = condition_select(girl_result,'girl')
    result = dict(man_dict,**girl_dict)
    return result
# 身高分组
@app.route('/api/stuw_height_count')
def gen_height_data():
    conn = utils.get_mysql_connection()
    try:
        with conn.cursor() as cursor:
            pass
        
    except pymysql.MySQLError() as err:
        main_log.error()
        main_log.error(err)
    finally:
        conn.close()



if __name__ == '__main__':
    app.run(debug=True)
