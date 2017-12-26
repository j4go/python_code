'''
假如一个网店制定了下述折扣规则：
1、 有 1000 或以上积分的顾客，每个订单享 5% 折扣。
2、 同一订单中，单个商品的数量达到 20 个或以上，享 10% 折扣。 
3、 订单中的不同商品达到 10 个或以上，享 7% 折扣。

简单起见，我们假定一个订单一次只能享用一个折扣。
'''



'''
上下文

　　把一些计算委托给实现不同算法的可互换组件，它提供服务。在这个电商示例中，上下文是 Order，它会根据不同的算法计算促销折扣。

策略

　　实现不同算法的组件共同的接口。在这个示例中，名为 Promotion 的抽象类扮演这个角色。

具体策略

　　“策略”的具体子类。fidelityPromo、BulkPromo 和 LargeOrderPromo 是这里实现的三个具体策略。

按照《设计模式：可复用面向对象软件的基础》一书的说明，具体策略由上下文类的客户选择。在这个示例 中，实例化订单之前，系统会以某种方式选择一种促销折扣策略，然后把它传给 Order 构造方法。
具体怎么选择策略，不在这个模式的职责范围内。

实现 Order 类，支持插入式折扣策略
'''


# from abc import ABC, abstractclassmethod
# from collections import namedtuple

# Customer = namedtuple('Customer', 'name fidelity')


# class LineItem:
#     '''购物车条目类 每个条目有属性：产品 价格 数量'''

#     def __init__(self, product, quantity, price):
#         self.product = product
#         self.quantity = quantity
#         self.price = price

#     def total(self):
#         '''购物车一个条目的总价'''
#         return self.price * self.quantity


# class Order:
#     '''订单类 客户 购物车 折扣 计算总价和应付款 '''

#     def __init__(self, customer, cart, promotion):
#         self.customer = customer
#         self.cart = list(cart)
#         self.promotion = promotion

#     def total(self):
#         '''打折前的总价'''
#         # if not hasattr(self, '__total'): # 为什么要加这句判断？
#         #     self.__total = sum(item.total() for item in self.cart)
#         # return self.__total
#         return sum(item.total() for item in self.cart)

#     def due(self):
#         '''打折后的应付款'''
#         if not self.promotion:
#             discount = 0
#         else:
#             discount = self.promotion.discount(self)
#         return self.total() - discount

#     def __repr__(self):
#         fmt = '<Order total: {:.2f} due: {:.2f}>'
#         return fmt.format(self.total(), self.due())



class Promotion(ABC):
    '''在 Python 3.4 中，声明抽象基类最简单的方式是子类化 abc.ABC。'''

    @abstractclassmethod
    def discount(self, order):
        pass


class FidelityPromo(Promotion):

    def discount(self, order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0



class BulkItemPromo(Promotion):

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount

class LargeOrderPromo(Promotion):

    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0



joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = [LineItem('banana', 4, .5), 
        LineItem('apple', 10, 1.5), 
        LineItem('watermellon', 5, 5.0)]
print(Order(joe, cart, FidelityPromo()))
print(Order(ann, cart, FidelityPromo()))
banana_cart = [LineItem('banana', 30, .5), 
                LineItem('apple', 10, 1.5)]
print(Order(joe, banana_cart, BulkItemPromo()))
long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
print(Order(joe, long_order, LargeOrderPromo()))
print(Order(joe, cart, LargeOrderPromo()))



'''
利用 Python 中作为对象的函数，可以使用更少的代码实现相同的功能。
每个具体策略都是一个类，而且都只定义了一个方法，即 discount。此外，策略实例没有状态（没有实例属性）。你可能会 说，它们看起来像是普通的函数——的确如此。可以把具体策略换成简单的函数，
去掉 Promotion 抽象类。用函数分别实现不同的促销策略，并把促销函数作为
参数传入即可。
以下是重构之后的实现。
'''




from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:
    '''购物车条目类 每个条目有属性：产品 价格 数量'''

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        '''购物车一个条目的总价'''
        return self.price * self.quantity


class Order:
    '''订单类 客户 购物车 折扣 计算总价和应付款 '''

    def __init__(self, customer, cart, promotion):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        '''打折前的总价'''
        # if not hasattr(self, '__total'): # 为什么要加这句判断？
        #     self.__total = sum(item.total() for item in self.cart)
        # return self.__total
        return sum(item.total() for item in self.cart)

    def due(self):
        '''打折后的应付款'''
        if not self.promotion:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())



def fidelity_promo(order):
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

def bulk_item_promo(order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

def large_order_promo(order):
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0


'''
用函数实现策略后，去掉了抽象类和策略类，代码更精简，也更加易读，
新的 Order 类使用起来更简单
'''

joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = [LineItem('banana', 4, .5), 
        LineItem('apple', 10, 1.5), 
        LineItem('watermellon', 5, 5.0)]
print(Order(joe, cart, fidelity_promo))
print(Order(ann, cart, fidelity_promo))
banana_cart = [LineItem('banana', 30, .5), 
                LineItem('apple', 10, 1.5)]
print(Order(joe, banana_cart, bulk_item_promo))
long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
print(Order(joe, long_order, large_order_promo))
print(Order(joe, cart, large_order_promo))

'''
具体策略一般没有内部状态，只是处理上下文中的数据。此时，一定要使用普通的函数，别去编写只有一 个方法的类，再去实现另一个类声明的单函数接口。函数比用户定义的 类的实例轻量，因为各个策略函数在 Python 编译模块时只会创建一次。普通的函数也是“可共享的对象，可以同时在多个上下文中使用”。
'''


'''
新的需求，帮用户自动选择最优惠的打折方式
迭代一个函数列表，并找出折扣额度最大的，以下是实现
'''

promos = [fidelity_promo, bulk_item_promo, large_order_promo]

def best_promo(order):
    return max(promo(order) for promo in promos) # 生成器表达式 简洁有力！

joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = [LineItem('banana', 4, .5), 
        LineItem('apple', 10, 1.5), 
        LineItem('watermellon', 5, 5.0)]
print(Order(joe, cart, best_promo))
print(Order(ann, cart, best_promo))
banana_cart = [LineItem('banana', 30, .5), 
                LineItem('apple', 10, 1.5)]
print(Order(joe, banana_cart, best_promo))
long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
print(Order(joe, long_order, best_promo))
print(Order(joe, cart, best_promo))


'''
以上函数列表的方式虽然简洁易读，但有容易被忽略的缺陷，新添加的促销策略，要添加到promos列表中，
否则出问题。
解决方案是利用内置函数globals():
globals()返回一个字典，表示当前的全局符号表。这个符号表始终针对当前 模块（对函数或方法来说，是指定义它们的模块，而不是调用它们的模块）。

借助globals 函数帮助 best_promo 自动找到其他可用的 *_promo 函数，实现如下：
'''

promos = [globals()[name] for name in globals()
            if name.endswith('_promo')
            and name != 'best_promo']

def best_promo(order):
    return max(promo(order) for promo in promos)

joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = [LineItem('banana', 4, .5), 
        LineItem('apple', 10, 1.5), 
        LineItem('watermellon', 5, 5.0)]
print(Order(joe, cart, best_promo))
print(Order(ann, cart, best_promo))
banana_cart = [LineItem('banana', 30, .5), 
                LineItem('apple', 10, 1.5)]
print(Order(joe, banana_cart, best_promo))
long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
print(Order(joe, long_order, best_promo))
print(Order(joe, cart, best_promo))


'''
以上的改进已经挺好的了，但其中有个小限制是要求策略函数都以_promo结果。
一种思路是既然要收集所有可用的促销函数，就可以在单独的模块中保存策略函数，
把best_promo排除在外。
要导入 promotions 模块，得用到高阶内省函数的 inspect 模块，
inspect.getmembers 函数用于获取对象（这里是 promotions 模块） 的属性，第二个参数是可选的判断条件（一个布尔值函数）。我们使用的是 inspect.isfunction，只获取模块中的函数。
实现如下:
'''


import promotion
import inspect

promos = [func for _, func in inspect.getmembers(promotion, inspect.isfunction)]

def best_promo(order):
    return max(promo(order) for promo in promos)

joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = [LineItem('banana', 4, .5), 
        LineItem('apple', 10, 1.5), 
        LineItem('watermellon', 5, 5.0)]
print(Order(joe, cart, best_promo))
print(Order(ann, cart, best_promo))
banana_cart = [LineItem('banana', 30, .5), 
                LineItem('apple', 10, 1.5)]
print(Order(joe, banana_cart, best_promo))
long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
print(Order(joe, long_order, best_promo))
print(Order(joe, cart, best_promo))

'''
修改后，经测试可以是行得通的，把策略函数的实现放到单独的模块，逻辑清晰，方便扩展，
定义函数也更加灵活自在，不必拘泥于函数名。到此可能会觉得已经改进得差不多了。但其实是有问题的。
promotions 模块只能包含计算订单折扣的函数！这是对代码的隐性假设。如果有人在 promotions 模块中使用不同的签名定义函数，那么 best_promo 函数尝试将其应用到订单上时会出错。
解决方案思路之一是可以添加更为严格的测试，审查传给实例的参数，进一步过滤函数。
(实际上以_promo结尾标记策略函数也有同样的问题。)

动态收集促销折扣函数更为显式的一种方案是使用简单的装饰器。

装饰器的一个关键特性是，它们在被装饰的函数定义之后立即运行。
这通常是在导入时(即 Python 加载模块时)而不是运行时。

promos 列表中的值使用 promotion 装饰器填充，代码重构如下：
'''



promos = []

def promotion(promo_func):
    promos.append(promo_func)
    return promo_func


@promotion
def fidelity_promo(order):
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

@promotion
def bulk_item_promo(order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

@promotion
def large_order_promo(order):
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0


def best_promo(order):
    return max(promo(order) for promo in promos)


joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = [LineItem('banana', 4, .5), 
        LineItem('apple', 10, 1.5), 
        LineItem('watermellon', 5, 5.0)]
print(Order(joe, cart, best_promo))
print(Order(ann, cart, best_promo))
banana_cart = [LineItem('banana', 30, .5), 
                LineItem('apple', 10, 1.5)]
print(Order(joe, banana_cart, best_promo))
long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
print(Order(joe, long_order, best_promo))
print(Order(joe, cart, best_promo))


'''
到此，得到了一个相对完美的解决方案。优点如下：
1、促销策略函数无需使用特殊的名称（即不用以 _promo 结尾）。
2、@promotion 装饰器突出了被装饰的函数的作用，还便于临时禁用某个促销策略：只需把装饰器注释掉。
3、促销折扣策略可以在其他模块中定义，在系统中的任何地方都行，只要使用 @promotion 装饰即可。
'''


