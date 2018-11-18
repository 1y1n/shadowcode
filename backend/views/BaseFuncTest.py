import tornado.web
from views import route
from handler.Base import *
import json

@route(r'/test')
class BaseTestHandler(BaseHandler):
    def get(self):
        # ret = tornado.escape.json_encode({'code': 0, 'data': 'This is a base handler.'})
        self.finish({'code': 0, 'data': 'This is a base handler.'})
    
    def post(self):
        rec_data = self.get_argument('data', '')
        # print(rec_data)
        if rec_data:
            self.finish({'code': 0, 'data': 'I have received the message.'})


@route(r'/test_test', kwargs=dict(rec_name='test_name'), name="121")  # kwargs 是URLSpec的用法，向class传入参数。class需要用initialize初始化
class TestHandler(tornado.web.RequestHandler):
    def initialize(self, rec_name):
        self.name = rec_name

    def get(self):
        self.write(f"This is a test handler. My name is {self.name}.")

@route(r'/test_login')
class TestLogin(tornado.web.RequestHandler):
    def get(self):
        # 应该是在用户登录提交表单部分设置cookie，也就是post。放在get只是测试
        self.set_secure_cookie("cookie_name", "cookie_value", expires_days=1)  # set cookie
        self.write(f"login test. Your cookie is {self.get_secure_cookie('cookie_name')}")

    @tornado.web.authenticated  # 检验是否登录的装饰器 相当于 if not self.current_user: self.redirect()
    def post(self):
        self.write("")


# 异步测试
# @route(r'async_test')
# class AsyncTest(tornado.web.RequestHandler):
#     pass