from flask import Blueprint, render_template, request, redirect
import pymysql  # 放这里
ac = Blueprint('account', __name__)
@ac.route('/')
def index():
    return render_template("login.html")
@ac.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    role = request.form.get("role")
    mobile = request.form.get("mobile")
    pwd = request.form.get("pwd")
    print(role, mobile, pwd)
    conn = pymysql.connect(
        host="localhost",
        user="root",
        passwd="11111111",
        db="xjgldm"
    )
    cursor = conn.cursor()
    # 重点修复：1. 加了=  2. 参数顺序对了
    sql = "select * from userinfo where role=%s and mobile=%s and password=%s"
    cursor.execute(sql, (role, mobile, pwd))  # 顺序必须对应
    user_dict = cursor.fetchone()
    cursor.close()
    conn.close()
    if user_dict:
        return redirect('/order/list')
    return render_template("login.html", error="用户名或密码错误")