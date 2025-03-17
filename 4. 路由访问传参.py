from flask import Flask

app = Flask(__name__)
config = {
    "host":"0.0.0.0",
    "debug":True,
    "port":5000
}
app.config.update(config)

# <格式: 变量参数>
# 支持的类型 default->string path int float any uuid
@app.route("/<int: userid>")
def index(userid):
    return f"{userid}"

if __name__ == '__main__':
    app.run()