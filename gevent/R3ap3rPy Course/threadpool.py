from gevent.threadpool import ThreadPool
import gevent
import time

pool = ThreadPool(5)
start = time.time()
for _ in range(10):
    pool.spawn(time.sleep, 1)
gevent.wait()
delay = time.time() - start
print(f"Running time.sleep(1) with 10 times with 5 from pool, took {delay} seconds!")
