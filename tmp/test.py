import collections

Card = collections.namedtuple('Card', 'rank suit')

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]


    def __len__(self):
        ''' 定义len() '''
        return len(self._cards)

    def __getitem__(self, position):
        ''' 定义下标index访问 '''
        return self._cards[position]



deck = FrenchDeck()

from random import choice
print(choice(deck))

# __len__
print(len(deck))

# __getitem__
print(deck[:3])
print(deck[12::13])

# 反向迭代 reversed 返回是迭代对象 注意同一个迭代对象只能遍历一次
# print(reversed(deck))
for card in reversed(deck):
    print(card)

# 迭代通常是隐式的，譬如说一个集合类型没有实现 __contains__ 方法，
# 那么in运算符就会按顺序做一次迭代搜索。于是，in运算符可以用在我们的
# FrenchDeck 类上，因为它是可迭代的：
print(Card('Q', 'hearts') in deck)
print(Card('Q', 'beasts') in deck)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    ''' 排序函数算法：52张牌 0-51 数值对应的下标x4+花色权值'''
    rank_value = FrenchDeck.ranks.index(card.rank)
    # print(rank_value, len(suit_values), suit_values[card.suit])
    return rank_value * len(suit_values) + suit_values[card.suit]


card = choice(deck)
print(card)
print(spades_high(card))

for card in sorted(deck, key=spades_high):
    print(card)
