import tornado.web
from views import route
from handler.Base import *
import base64
import binascii

###############
# 小工具
# pycipher
# rot13
# playfair
# caesar
# autokey
###############
@route('/base_crypto')
class BaseCode(BaseHandler):
    def get(self):
        rec_crypt = self.get_argument("crypt", "")
        rec_type = self.get_argument("type", "")
        rec_data = self.get_argument("data", "")

        if rec_crypt and rec_type and rec_data:
            self.convert(rec_crypt, rec_type, rec_data)

        else:
            self.finish({'code': 1})

    def convert(self, rec_crypt, rec_type, rec_data):
        try:
            if rec_crypt == 'encode':
                if rec_type == 'base64':
                    self.finish({'code': 0, 'data': base64.b64encode(rec_data.encode('utf-8')).decode('utf-8')})
                elif rec_type == 'base32':
                    self.finish({'code': 0, 'data': base64.b32encode(rec_data.encode('utf-8')).decode('utf-8')})
                elif rec_type == 'base16':
                    self.finish({'code': 0, 'data': base64.b16encode(rec_data.encode('utf-8')).decode('utf-8')})
            elif rec_crypt == 'decode':
                if rec_type == 'base64':
                    self.finish({'code': 0, 'data': base64.b64decode(rec_data.encode('utf-8')).decode('utf-8')})
                elif rec_type == 'base32':
                    self.finish({'code': 0, 'data': base64.b32decode(rec_data.encode('utf-8')).decode('utf-8')})
                elif rec_type == 'base16':
                    self.finish({'code': 0, 'data': base64.b16decode(rec_data.encode('utf-8')).decode('utf-8')})
        except binascii.Error:
            self.finish({'code': 0, 'data': 'input error.'})
        except:
            self.finish({'code': 0, 'data': 'server error.'})



@route('/T')
class T(tornado.web.RequestHandler):
    pass