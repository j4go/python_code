# _*_ coding: utf-8 _*_


class C(object):

    code = 'for my life'
    _t = '_t'
    __tt = '__t'

    def func(self):
        print('Coding {}!'.format(self.code))

    @property
    def proper(self):
        print('Coding {}!'.format(self.code))

    @classmethod
    def clsfunc(cls):
        print('Coding {}!'.format(C.code))
        cls().func()

    @staticmethod
    def staticfunc():
        print('Coding {}!'.format(C.code))


if __name__ == '__main__':
    c = C()
    # c.proper
    # print(c._t)
    # c.func()
    # c.clsfunc()
    # c.staticfunc()
    print(dir(C))
    print(C.__dict__)
    print(C._C__tt)
