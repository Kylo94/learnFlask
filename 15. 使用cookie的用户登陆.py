import json
from flask import Flask, request, redirect, url_for, session, make_response, render_template

app = Flask(__name__)
app.secret_key = "hello"

"""cookie的基本使用"""
@app.route("/api/set_cookie")
def set_cookie():
    """cookie的设置"""
    # cookies是保存到客户端的
    response = make_response("设置cookies")
    response.set_cookie("user_id", '100')
    # 设置cookie的有效时间
    response.set_cookie("username", 'kylo', max_age=60)
    return response

@app.route("/api/get_cookie")
def get_cookie():
    """获取cookie"""
    return request.cookies

@app.route("/api/del_cookie")
def del_cookie():
    # cookie保存在客户端中，服务器无法删除
    # 通知浏览器cookie过期
    response = make_response("删除cookie")
    response.set_cookie("username",max_age=0)
    return response

@app.route("/")
def index():
    username = request.cookies.get('username')
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
        response.set_cookie("username", username, max_age=10)
        return response
    else:
        url = url_for('login')
        response = redirect(url)
        # response.status = 400
        return response

@app.route('/<username>')
def user(username):
    if request.cookies.get('username'):
        return f"用户{username}"
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

