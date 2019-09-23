# -*- coding: utf-8 -*-

from pokerSimulator import Card, Deck, Player
from pokerSimulator.checkHands import four_of_a_kind, pair, twoPair, highCard, threeOfAKind,royal_flush,get_card_value_count


d = Deck()
d.shuffle()

p1 = Player('p1')
a = [Card('Hearts',5),Card('Clubs',5),Card('Spades',10),Card('Diamonds',1),Card('Hearts',3)]
b = [Card('Hearts',4),Card('Clubs',4),Card('Spades',14),Card('Diamonds',5),Card('Hearts',3)]
c = [Card('Hearts',4),Card('Clubs',4),Card('Spades',6),Card('Diamonds',4),Card('Hearts',2)]

f = [Card('Clubs',10),Card('Clubs',11),Card('Clubs',12),Card('Clubs',13),Card('Clubs',14)]


e = [Card('Hearts',4),Card('Clubs',4),Card('Spades',3),Card('Diamonds',3),Card('Hearts',5)]
hand = twoPair(e)

print(hand._is_flush())
print([count for val,count in get_card_value_count(c)])
