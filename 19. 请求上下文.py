from flask import Flask, request, session, current_app
app = Flask(__name__)
app.config["SECRET_KEY"] = "my secret key"

@app.route('/')
def index():
    # 在视图的上下文环境当中
    # 会刷新 request对象以及session对象
    # 只能在视图的context上下文中使用
    print(request)
    print(session)
    return 'ok'


if __name__ == '__main__':
    app.run(debug=True)

