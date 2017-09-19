# coding: utf-8
def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY-i):
            return True
    return False

# 测试uubntu mono字体


def queens(num=8, state=()):
    if len(state) == num-1:
        for pos in range(num):
            if not conflict(state, pos):
                yield (pos,)
    else:
        for pos in range(num):
            if not conflict(state, pos):
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result

print len(list(queens(8)))
