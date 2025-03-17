from flask import Flask,request

app = Flask(__name__)

@app.route('/header')
def header():
    print(request.headers)
    print(request.headers.get('User-Agent'))
    print(request.user_agent)
    """获取自定义请求头"""
    print(request.headers.get('company'))
    return '获取请求头信息'

if __name__ == '__main__':
    app.run(debug=True)

