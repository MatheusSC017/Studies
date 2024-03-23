from gevent import Greenlet


def inside():
    print(f"We are inside the context manager!")
    return 99


with Greenlet.spawn(inside) as g:
    print(f"Entered the context manager!")

print(g.get(block=False))
