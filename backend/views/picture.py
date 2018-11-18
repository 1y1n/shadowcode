import tornado.web
from views import route


# 处理图像相关
@route('/picture')
class Picture(tornado.web.RequestHandler):
    pass
 