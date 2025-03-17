import json

from flask import Flask, request, redirect, url_for

app = Flask(__name__)


@app.route("/sms/<int:mob>")
def sms(mob):
    return f"用户{mob}发送了消息"

@app.route("/")
def index():
    return redirect(url_for('sms', mob="1234"))


if __name__ == '__main__':
    app.run(debug=True)

