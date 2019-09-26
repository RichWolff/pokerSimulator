# -*- coding: utf-8 -*-

from pokerSimulator import Card, Deck, Player
from pokerSimulator.checkHands import highCard, pair, twoPair, threeOfAKind, straight, flush, fullHouse, four_of_a_kind, strait_flush, royal_flush,get_card_value_count,WrongHandError
from itertools import combinations

d = Deck()
d.shuffle()

p1 = Player('p1')

rf = [Card('Clubs',10),Card('Clubs',11),Card('Clubs',12),Card('Clubs',13),Card('Clubs',14)]
sf = [Card('Clubs',10),Card('Clubs',11),Card('Clubs',12),Card('Clubs',13),Card('Clubs',9)]
foak = [Card('Hearts',5),Card('Clubs',5),Card('Spades',5),Card('Diamonds',5),Card('Hearts',3)]
fh = [Card('Hearts',5),Card('Clubs',5),Card('Spades',5),Card('Diamonds',1),Card('Hearts',1)]
flsh = [Card('Clubs',2),Card('Clubs',5),Card('Clubs',12),Card('Clubs',13),Card('Clubs',9)]
strt = [Card('Hearts',10),Card('Diamonds',11),Card('Clubs',12),Card('Clubs',13),Card('Clubs',9)]
strtLow = [Card('Hearts',4),Card('Clubs',2),Card('Spades',14),Card('Diamonds',5),Card('Hearts',3)]
toak = [Card('Hearts',5),Card('Clubs',5),Card('Spades',5),Card('Diamonds',1),Card('Hearts',3)]
tp = [Card('Hearts',4),Card('Clubs',4),Card('Spades',3),Card('Diamonds',3),Card('Hearts',5)]
p = [Card('Hearts',4),Card('Clubs',4),Card('Spades',3),Card('Diamonds',2),Card('Hearts',5)]
hc = [Card('Hearts',4),Card('Clubs',2),Card('Spades',13),Card('Diamonds',5),Card('Hearts',3)]


hand = royal_flush(rf)
hand._check_hand()
    
handCheckOrder = [royal_flush, strait_flush, four_of_a_kind, fullHouse, flush, straight, threeOfAKind, twoPair, pair, highCard]
highestHand = ()


hand = [d.drawCard() for _ in range(7)]
allPossibleHands = combinations(hand,5)

highestHand = []
for hand in allPossibleHands:
    
    for checkHand in handCheckOrder:
        handType = checkHand(hand)
        if handType._check_hand():
            break
        
    highestHand.append([handType.score,handType.cards])

print(sorted(highestHand,key=lambda x: -x[0])[:1])

toak = [Card('Hearts',5),Card('Clubs',5),Card('Spades',5),Card('Diamonds',1),Card('Hearts',3)]
toak2 = [Card('Hearts',5),Card('Clubs',5),Card('Spades',5),Card('Diamonds',2),Card('Hearts',3)]


fh1 = threeOfAKind(toak)
fh2 = threeOfAKind(toak2)
print(fh1.three,fh2.three)
print(fh1.high1,fh2.high1)
print(fh1.high2,fh2.high2)

print(sorted([fh1.cards,fh2.cards],reverse=True))