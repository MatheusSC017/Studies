import gevent


class MyGreenlet(gevent.Greenlet):
    def __init__(self, seconds):
        gevent.Greenlet.__init__(self)
        self.seconds = seconds

    def _run(self):
        gevent.sleep(self.seconds)

    def __str__(self):
        return f"MyGreenlet({self.seconds})"
