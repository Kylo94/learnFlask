import json
import os
from datetime import timedelta

from flask import Flask, request, redirect, url_for, session, make_response, render_template

app = Flask(__name__)
app.secret_key = os.urandom(24)

# session会话
# 一般情况下我们会将一些重要信息储存到服务器
@app.route('/set_session')
def set_session():
    session["username"] = "root"
    session["userid"] = 84
    return "set session"

@app.route('/get_session')
def get_session():
    print(session.get('userid'))
    print(session.get('username'))
    return "get session"

@app.route('/del_session')
def del_session():
    del session['username']
    del session['userid']
    return "del_session"

@app.route("/")
def index():
    username = session.get('username')
    if username:
        url = url_for('user', username= username)
        return redirect(url)
    return redirect('/login')

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == "GET":
        return render_template('form.html')
    # 接收post表单
    username = request.form.get('username')
    pwd = request.form.get('pwd')
    # 验证用户名密码
    if username == "root" and pwd == "root":
        response = make_response("登录成功", 302, {'location': '/'})
        session["username"] = username
        # session持久化
        session.permanent = True
        app.config.update({'PERMANENT_SESSION_LIFETIME':timedelta(days=7)})
        print(app.config)
        return response
    else:
        url = url_for('login')
        response = redirect(url)
        response.status = 400
        return response

@app.route('/<username>')
def user(username):
    if session.get('username'):
        return f"用户{username}"
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

