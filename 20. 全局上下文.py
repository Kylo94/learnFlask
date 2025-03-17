from flask import Flask, current_app, g
app = Flask(__name__)
app.config["SECRET_KEY"] = "my secret key"

def t1():
    g.name = "123"
def t2():
    print(g.name)

@app.route('/')
def index():
    # 本地代理 app 对象
    print(app)
    print(current_app)
    print(app == current_app)
    print(app is current_app)
    print(app.url_map)
    print(current_app.url_map)
    # 针对于本次请求的一个全局变量 g
    t1()
    t2()
    return 'ok'


if __name__ == '__main__':
    with app.app_context():
        print(current_app)
    app.run(debug=True)

