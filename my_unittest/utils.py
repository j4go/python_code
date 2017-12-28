
def to_str(data):
    """Tansform data to a str"""
    if isinstance(data, str):
        return data
    elif isinstance(data, bytes):
        return data.decode('utf-8')
    else:
        raise TypeError('Must supply str or bytes,'
                        'found: %r' % data)


# def test_to_str():
#     assert to_str('hello') == 'hello'