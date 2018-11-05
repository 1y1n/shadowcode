import tornado.ioloop
import tornado.web
from base import app
import BaseFuncTest



if __name__ == '__main__':
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

