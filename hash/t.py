class A(object):
    def func(self, arg="hi"):
        print('aaa func')

class B(A):
    def func(self, arg="abc"):
        # super(B, self).func(arg)
        print('bbb func')

b = B()
b.func()
