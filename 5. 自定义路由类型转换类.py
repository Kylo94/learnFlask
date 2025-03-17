# 基于正则进行匹配
# 导入转换器基类
from werkzeug.routing import BaseConverter
from flask import Flask
# 定义转换类继承基类
class MobileConverter(BaseConverter):
    regex = r"^1[3-9]+\d{9}"

app = Flask(__name__)
config = {
    "HOST":"0.0.0.0",
    "DEBUG":True,
    "PORT":5000
}
app.config.update(config)
# 注册到app的转换字典中
app.url_map.converters['mob'] = MobileConverter

@app.route("/sms/<mob:mobile>")
def sms(mobile):
    return f"发送短信给:{mobile}用户"

if __name__ == '__main__':
    app.run()