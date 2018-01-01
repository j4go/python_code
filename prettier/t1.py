"""
更好的代码重构示例。
"""


def dispatch_if(operator, x, y):
    """分支很多的情况下使用if代码冗长也不美观。
    查找效率也低下。
    """
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y
    return None


print(dispatch_if('mul', 2, 3))


def dispatch_dict(operator, x, y):
    """如果分支有很多很多的话，用字典查找可以提高效率。
    在这种情况下，函数可以用lamda实现，看起来简洁。
    """
    return {
        'add': lambda : x + y,
        'sub': lambda : x - y,
        'mul': lambda : x * y,
        'div': lambda : x / y,
    }.get(operator, lambda : None)()


print(dispatch_dict('div', 2, 3))


# 从可读性来说if更简单易懂
