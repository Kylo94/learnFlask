from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>这是一个主页</h1>"

# 设置环境变量：
# export FLASK_DEBUG=True 发开模式；=false 发布模式
# export FLASK_APP=app.py 启动文件
# flask run 启动程序
# flask run --port=8888 指定端口

# 使用命令窗口启动时，不会经过该判断
if __name__ == '__main__':
    print(app.config)
    app.run()

