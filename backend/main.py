import tornado.ioloop
import tornado.web
from app import app

import views._views

if __name__ == '__main__':
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

