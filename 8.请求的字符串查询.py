from flask import Flask,request
from urllib.parse import unquote, parse_qs

app = Flask(__name__)

@app.route('/qs')
def qs():
    # 可以获取get请求参数，数据为字节数据
    # python原生处理字符串
    # print(parse_qs(request.query_string.decode()))
    # 获取单个参数值
    # flask 的 request 处理args
    # print(request.args['age'])
    # 获取多个参数值
    # 请求url = "http://127.0.0.1:5000/qs?user=%E5%B0%8F%E6%98%8E&age=16&fav=shopping&fav=eat"
    print(request.args.getlist("fav"))
    return "<h1>这是一个主页</h1>"

if __name__ == '__main__':
    app.run(debug=True)

