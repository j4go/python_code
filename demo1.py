# simple
def validate(name):
    if len(name) < 8:
        raise ValueError # or raise ValueError()

# better
def validate1(name):
    if len(name) < 8:
        raise ValueError('Name too short: {}'.format(name))

# more specific customerize exception
class NameTooShortError(ValueError):
    pass

def validate2(name):
    if len(name) < 8:
        raise NameTooShortError(name)

# print(validate('molock'))
# print(validate1('molock'))
print(validate2('molock'))