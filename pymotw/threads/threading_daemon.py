import threading
import time
import logging


def daemon():
    logging.debug('Starting')
    time.sleep(0.2)
    logging.debug('Exiting')


def non_daemon():
    logging.debug('Starting')
    # time.sleep(0.2)
    logging.debug('Exiting')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

# a daemon that runs without blocking the main program from exiting
d = threading.Thread(name='daemon', target=daemon, daemon=True)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()


"""
The output does not include the "Exiting" message from the 
daemon thread, since all of the non-daemon threads 
(including the main thread) exit before the daemon thread 
wakes up from the sleep() call.
"""
