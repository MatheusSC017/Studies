import gevent

g = gevent.spawn(1/0)
g.join()
gevent.sleep(3)
