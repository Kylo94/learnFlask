import json
import os
from datetime import timedelta

from flask import Flask, request, redirect, url_for, session, make_response, render_template

app = Flask(__name__)

@app.before_request
def before():
    """
    触发时机：在路由匹配成功后、视图函数执行前触发。
    参数：无参数，但可通过 request 对象访问请求数据（如方法、头、表单等）。
    返回值：必须返回 None，若返回非 None（如响应对象），会直接终止请求流程。
    适用场景：鉴权、请求校验、统一参数处理、性能监控等。
    """
    print("在路由匹配成功后、视图函数执行前触发")
    return None

# app.before_request.append(before)

@app.route('/')
def index():
    print("-"*10+'视图执行了'+"-"*10)
    return 'ok'

@app.after_request
def after(response):
    """
    触发时机：在视图函数返回响应后、实际发送响应前执行。
    参数：接收 response 对象，可修改响应头或状态码。
    返回值：必须返回 response，否则引发错误。
    适用场景：添加统一响应头、日志记录、错误处理等。
    """
    print("在视图函数返回响应后、实际发送响应前执行")
    return response

@app.teardown_request
def teardown():
    """
    触发时机：在视图函数执行完成后（无论是否抛出异常）。在 @app.after_request 之后触发。
    参数：接收 exception 参数（若请求过程中发生异常，则为异常对象；否则为 None）。
    返回值：无返回值。
    适用场景：资源释放（如关闭数据库连接、释放文件）、事务回滚、错误上下文清理等。
    """
    print("视图执行结束")

if __name__ == '__main__':
    app.run(debug=True)

