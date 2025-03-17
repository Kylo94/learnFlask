import json

from flask import Flask, request, redirect, url_for

app = Flask(__name__)
@app.route("/jump")
def jump():
    # return redirect("https://www.baidu.com", 302)
    return "", 302, {'location': "https://www.baidu.com"}

if __name__ == '__main__':
    app.run(debug=True)

