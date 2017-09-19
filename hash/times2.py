def times2(value):
    """
    Multiplies the provided value by two.
    Because input objects can override the behavior of
    multiplication, the result can be different depending
    on the type of object passed in.

    >>> times2(5)
    10
    >>> times2('test')
    'testtest'
    >>> times2(('a', 1))
    ('a', 1, 'a', 1)

    """
    return value * 2


if __name__ == '__main__':
    import doctest
    doctest.testmod()
