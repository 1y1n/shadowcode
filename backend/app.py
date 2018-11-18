import tornado.web


def make_app():
    settings = {
        'debug': True,  # auto reload
        'cookie_secret': "this is a secret cookie",
        #'login_url': "/login",  # 未登录用户跳转
        'xsrf_cookie': True,  # XSRF防护
    }
    
    return AppInit([], **settings) # 初始化路由需要置空
    # return tornado.web.Application([
    #     (r"/", BaseHandle),
    #     (r"/login", TestLogin),
    #     tornado.web.URLSpec(r"/test", TestHandler, dict(name="121"))  # url 可以传入参数
    # ], **settings)


# reference: https://www.jb51.net/article/105494.htm
class AppInit(tornado.web.Application):  # 继承application对象

    def route(self, url, kwargs=None, name=None):
        def register(handler):
            self.add_handlers(".*$", [tornado.web.URLSpec(url, handler, kwargs=kwargs, name=name)])
        return register

app = make_app()
