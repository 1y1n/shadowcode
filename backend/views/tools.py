import tornado.web
from views import route
import base64


###############
# 小工具
# pycipher
# rot13
# playfair
# caesar
# autokey
###############
@route('/base64')
class BaseCode(tornado.web.RequestHandler):
    def get(self):
        rec_base64 = self.get_argument("base64", "")
        rec_base32 = self.get_argument("base32", "")
        rec_base16 = self.get_argument("base16", "")
        if rec_base64:
            self.write("base64")
        elif rec_base32:
            self.write("base32")
        elif rec_base16:
            self.write("base16")
        else:
            self.write("error")


@route('/T')
class T(tornado.web.RequestHandler):
    pass