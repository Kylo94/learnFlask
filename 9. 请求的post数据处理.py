from flask import Flask,request
from urllib.parse import unquote, parse_qs

app = Flask(__name__)

@app.route("/form1", methods=['GET','POST'])
def form_data():
    print(request.form.get('username')) # 获取表单单个数据
    print(request.form.getlist('fav')) # 获取表单多个数据
    print(request.files.get('pic')) # 获取单个文件 FileStorage
    print(request.files.getlist('pic')) # 获取多个文件 FileStorage
    return "表单数据"

@app.route("/data", methods='post')
def data():
    print(request.is_json) # 本次客户端提交的数据是否为json
    if request.is_json:
        print(request.json)

    print(request.data) # 获取客户端提交的原始数据
    return "Ajax"


if __name__ == '__main__':
    app.run(debug=True)

