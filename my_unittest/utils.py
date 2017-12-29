"""
Test example
code for testing

Testing is important
Testing is hard: code/isolation/fixtures/indirect value
"""

def to_str(data):
    """Tansform data to a str"""
    if isinstance(data, str):
        return data
    elif isinstance(data, bytes):
        return data.decode('utf-8')
    else:
        raise TypeError('Must supply str or bytes,'
                        'found: %r' % data)


def test_to_str():
    assert to_str('hello') == 'hello'


def encode(input_string):
    if not input_string:
        return []
    count = 1
    prev = ''
    lst = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev, count)
                lst.append(entry)
            count = 1
            prev = character
        else:
            count += 1
    else:
        entry = (character, count)
        lst.append(entry)
    return lst


def decode(lst):
    q = ''
    for character, count in lst:
        q += character * count
    return q