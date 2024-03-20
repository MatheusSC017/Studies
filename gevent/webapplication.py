from gevent import monkey
monkey.patch_all()
from gevent.pywsgi import WSGIServer
import random
import time
import web

urls = (
    "/", "index",
    "/long", "long_polling",
    "/verylong", "very_long_polling"
)


class index(object):
    def GET(self):
        return "<h1>Default context route</h1>"


class long_polling(object):
    def GET(self):
        waittime = random.randint(1, 5)
        time.sleep(waittime)
        return f"<h1>Long polling: {waittime}</h1>"


class very_long_polling(object):
    def GET(self):
        waittime = random.randint(10, 20)
        time.sleep(waittime)
        return f"<h1>Very Long polling: {waittime}</h1>"


application = web.application(urls, globals()).wsgifunc()
print(f"Serving on port 8080...")
WSGIServer(('127.0.0.1', 8080), application).serve_forever()
