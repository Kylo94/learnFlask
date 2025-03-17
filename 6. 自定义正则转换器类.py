from flask import Flask

app = Flask(__name__)
config = {
    "HOST":"0.0.0.0",
    "DEBUG":True,
    "PORT":5000
}
app.config.update(config)

from werkzeug.routing import BaseConverter
class RegexConverter(BaseConverter):
    def __init__(self, map, *args, **kwargs):
        super().__init__(map, *args, **kwargs)
        self.regex = args[0]
app.url_map.converters['regex'] = RegexConverter

@app.route(r"/sms/<regex('^1[3-9]\d{9}'):mobile>")
def sms(mobile):
    return f"发送短信给:{mobile}用户"

if __name__ == '__main__':
    app.run()