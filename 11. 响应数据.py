import json

from flask import Flask, make_response, render_template, Response, jsonify

app = Flask(__name__)
"""
1. 接收客户端请求
2. 根据请求操作文件
3. 相应请求处理结果
"""
@app.route('/')
def index():
    # 文本返回默认为html格式, 响应状态码
    # return 'hello world', 200
    # response = make_response("hello world", 200)
    # return response
    # return make_response("hello world", 200)
    # return render_template('index.html', id=10)
    pass

@app.route('/api/json')
def api_json():
    data = {"name":"xiaoming", "age":10}
    # response= Response(json.dumps(data), 200, {'content-type':'application/json'})
    # return response
    # return json.dumps(data), 200, {'content-type':'application/json'}
    # return jsonify(data)
    pass

@app.route('/api/image')
def api_image():
    with open('/pic.png') as file:
        data = file.read()
    # return Response(data, 200, {'Content-Type':'image/png'})
    return data, 200, {'Content-Type':'image/png'}

if __name__ == '__main__':
    app.run(debug=True)

