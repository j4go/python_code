class Averager():

    def __init__(self):
        self.series = []

    def __call__(self, new_value): # 实例是可调用对象
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)

def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager