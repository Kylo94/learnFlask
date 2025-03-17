import json

from flask import Flask, request, redirect, url_for

app = Flask(__name__)
@app.route("/user")
def index():
    if request.args.get('token'):
        return "个人中心"
    # return redirect('/login')
    # url = url_for('视图名称')
    # 路由列表
    print(app.url_map)
    return redirect(url_for('login'))
@app.route("/login")
def login():
    return "login"

if __name__ == '__main__':
    app.run(debug=True)

