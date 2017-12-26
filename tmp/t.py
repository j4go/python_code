# Meaning and logic separation
# 函数应该专注做某件事并且做到最好

# def elapse(year):
#     days = 365
#     if is_leap(year):
#         days += 1
#     for day in range(1, days + 1):
#         print('Day {} of {}'.format(day, year))

# def is_leap(year):
#     return year % 4 == 0 or (year % 100 == 0 and year % 400 == 0)


# elapse(2020)


# About asyncio
import asyncio

'''
Yury Selivanov - async/await in Python 3.5 and why it is awesome

[EuroPython 2016]
[21 July 2016]
[Bilbao, Euskadi, Spain]


pep 492 作者

async/await is here, everybody can use it in Python 3.5.  It's great
and awesome, yet only a few understand it.  As a PEP 492 author, I'd
really like to have a chance to better explain the topic, show why
async/await is important and how it will affect Python. I'll also tell
a story on how I worked on the PEP -- starting from an idea that I
discussed with Guido on PyCon US 2015, and landing to CPython source
code one and a half moths later!



asyncio is simple

asyncio.get_event_loop()
loop.create_task()
loop.run_until_complete() and loop.run_forever()
asyncio.gather()
loop.run_in_executor()
loop.close()

'''

'''
loop.create_task()

Wraps coroutines in a "coroutine runner": a
mechanism for the event loop to work with
async/await.
'''



# async def say(what, when):
#     print('start to say')
#     await asyncio.sleep(when)
#     print(what)
#     print('finish say')

# loop = asyncio.get_event_loop()
# loop.create_task(say('hello', 2.5))
# loop.create_task(say('world', 5))
# loop.run_forever()


'''
loop.gather()

Awaits on multiple coroutines(or tasks, or futures.)
'''
# async def say(what, when):
#     print('start to say')
#     await asyncio.sleep(when)
#     print(what)
#     print('finish say')

# loop = asyncio.get_event_loop()
# t1 = loop.create_task(say('hello', 2.5))
# t2 = loop.create_task(say('world', 5))
# loop.run_until_complete(
#     asyncio.gather(t1, t2))


'''
loop.run_in_executor()

Runs slow CPU-intensive or blockong IO code in a
thread or in a process pool.
'''

# def compute_pi(digits):
#     # implementation
#     return result

# await loop.run_in_executor(
#     None, compute_pi, 20000)

# # .. or ..

# pool = concurrent.futures.ProcessPoolExecutor()
# await loop.run_in_executor(
#     pool, compute_pi, 20000)



'''
loop.close()

Shuts down the event loop and frees resources.
'''


# async def say(what, when):
#     print('start to say')
#     await asyncio.sleep(when)
#     print(what)
#     print('finish say')

# loop = asyncio.get_event_loop()
# t1 = loop.create_task(say('hello', 2.5))
# t2 = loop.create_task(say('world', 5))

# try:
#     loop.run_until_complete(
#         asyncio.gather(t1, t2))
# finally:
#     loop.close()


'''
asyncio: debugging

PYTHONASYNCIODEBUG=1 python program.py
or loop.set_debug()

Configure python logging to see errors.

Configre your test runner to print out warnings.
'''




'''
Miguel Grinberg Asynchronous Python for the Complete Beginner PyCon 2017

"Speaker: Miguel Grinberg

With the introduction of the asyncio package in Python 3.4, you can hear lots of people talking about asynchronous programming, most in a favorable way, some not so much. In this talk, I will tell you what this async fever is about and what can it do for you that regular Python can't, not only with asyncio, but also with other frameworks that existed long before it.

Slides can be found at: https://speakerdeck.com/pycon2017 and https://github.com/PyCon/2017-slides"
'''


"""
Standard(synchronous) Python
"""

# from time import sleep
# from gevent import
from eventlet import sleep

def hello():
    print('Hello')
    sleep(2)
    print('World')

if __name__ == '__main__':
    hello()
    hello()
    hello()


"""
Asyncio
"""

# async def hello():
#     print('Hello')
#     await asyncio.sleep(2)
#     print('World')

# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     t1 = loop.create_task(hello())
#     t2 = loop.create_task(hello())
#     t3 = loop.create_task(hello())
#     task_group = asyncio.gather(t1, t2, t3)
#     try:
#         loop.run_until_complete(task_group)
#     finally:
#         loop.close()




"""
asyncio.sleep(0)

To tell the loop to return control back as soon as possible

Blocking library functions are incompatible with
async frameworks such as:
socket.*
select.*
subprocess.*
os.waitpid
threading.*
multiprocessing.*
time.sleep

All async frameworks provide non-blocking replacements
for these

Eventlet and Gevent can 'monkey-patch' the standard library
to make it async compatible
"""





