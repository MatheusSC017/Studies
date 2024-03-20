import os
from gevent.pywsgi import WSGIServer
from gevent import socket


def application(env, start_response):
    assert env
    start_response('200 OK', [])
    return []


listener = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
socketname = './' + os.path.basename(__file__) + '.sock'
if os.path.exists(socketname):
    os.remove(socketname)
listener.bind(socketname)
listener.listen(1)
WSGIServer(listener, application).serve_forever()
