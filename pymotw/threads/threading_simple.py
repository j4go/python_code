
from threading import Thread

def worker(num):
    """thread worker function"""
    print('Worker: %s' % num)


# threads = []
# for i in range(5):
#     t = Thread(target=worker)
#     threads.append(t)
#     t.start()

for i in range(5):
    # Thread(target=worker(i)).start()
    Thread(target=worker, args=(i,)).start()