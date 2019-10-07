# -*- coding: utf-8 -*-
from .checkHands import highCard, pair, twoPair, four_of_a_kind, get_card_value_count, getBestHand
from .card import Card


## Potential Hands
rf = [Card('Clubs',10),Card('Clubs',11),Card('Clubs',12),Card('Clubs',13),Card('Clubs',14)]
sf = [Card('Clubs',10),Card('Clubs',11),Card('Clubs',12),Card('Clubs',13),Card('Clubs',9)]
foak = [Card('Hearts',5),Card('Clubs',5),Card('Spades',5),Card('Diamonds',5),Card('Hearts',3)]
fh = [Card('Hearts',5),Card('Clubs',5),Card('Spades',5),Card('Diamonds',2),Card('Hearts',2)]
flsh = [Card('Clubs',2),Card('Clubs',5),Card('Clubs',12),Card('Clubs',13),Card('Clubs',9)]
strt = [Card('Hearts',10),Card('Diamonds',11),Card('Clubs',12),Card('Clubs',13),Card('Clubs',9)]
strtLow = [Card('Hearts',4),Card('Clubs',2),Card('Spades',14),Card('Diamonds',5),Card('Hearts',3)]
toak = [Card('Hearts',5),Card('Clubs',5),Card('Spades',5),Card('Diamonds',2),Card('Hearts',3)]
tp = [Card('Hearts',4),Card('Clubs',4),Card('Spades',3),Card('Diamonds',3),Card('Hearts',5)]
p = [Card('Hearts',4),Card('Clubs',4),Card('Spades',3),Card('Diamonds',2),Card('Hearts',5)]
hc = [Card('Hearts',4),Card('Clubs',2),Card('Spades',13),Card('Diamonds',5),Card('Hearts',3)]
        
foak_a = four_of_a_kind([Card('Hearts',14),Card('Spades',14),Card('Diamonds',14),Card('Clubs',14),Card('Hearts',10)])
foak_b = four_of_a_kind([Card('Hearts',13),Card('Spades',13),Card('Diamonds',13),Card('Clubs',13),Card('Hearts',10)])
foak_c = four_of_a_kind([Card('Hearts',2),Card('Spades',2),Card('Diamonds',2),Card('Clubs',2),Card('Hearts',14)])



class baseTest:
    def test_equality(self):
        def test_equality(a,b):
            assert a == b
            
class testFour(baseTest):
    def test_equality(self):
        assert foak_a == foak_a
    
class TestFourOfAKind:
    def test_equality(self):
        assert foak_a == foak_a
        
    def test_sort(self):
        assert foak_a > foak_b
        assert foak_b < foak_a
        assert foak_c < foak_a
        assert foak_c < foak_b
        assert foak_a > foak_c
        
        
twoPair_a = [Card('Hearts',14),Card('Spades',14),Card('Diamonds',13),Card('Clubs',13),Card('Hearts',5)]
twoPair_b = [Card('Hearts',12),Card('Spades',12),Card('Diamonds',11),Card('Clubs',11),Card('Hearts',8)]
twoPair_c = [Card('Hearts',12),Card('Spades',12),Card('Diamonds',10),Card('Clubs',10),Card('Hearts',9)]
twoPair_d = [Card('Hearts',12),Card('Spades',12),Card('Diamonds',10),Card('Clubs',10),Card('Hearts',5)]

class TestTwoPair:
    def test_bestHand(self):
        assert getBestHand(twoPair_a)[0] == 3
        assert getBestHand(twoPair_b)[0] == 3
        assert getBestHand(twoPair_c)[0] == 3
        assert getBestHand(twoPair_d)[0] == 3
        
    def test_equality(self):
        assert twoPair(twoPair_a) == twoPair(twoPair_a)
    
    def test_inequality(self):
        assert not twoPair(twoPair_a) == twoPair(twoPair_b)
        
    def test_sort(self):
        assert twoPair(twoPair_a) > twoPair(twoPair_b) > twoPair(twoPair_c) > twoPair(twoPair_d)
    
    def test_badSort(self):
        assert not twoPair(twoPair_a) < twoPair(twoPair_b) < twoPair(twoPair_c) < twoPair(twoPair_d)
        
pair_a = [Card('Hearts',5),Card('Clubs',5),Card('Spades',10),Card('Hearts',3),Card('Diamonds',2)]
pair_b = [Card('Hearts',4),Card('Clubs',4),Card('Spades',14),Card('Diamonds',5),Card('Hearts',3)]
pair_c = [Card('Hearts',4),Card('Clubs',4),Card('Spades',8),Card('Diamonds',5),Card('Hearts',2)]
pair_e = [Card('Hearts',4),Card('Clubs',4),Card('Spades',8),Card('Diamonds',3),Card('Hearts',2)]

class TestPair:
    def test_bestHand(self):
        assert getBestHand(pair_a)[0] == 2
        assert getBestHand(pair_b)[0] == 2
        assert getBestHand(pair_c)[0] == 2
        assert getBestHand(pair_e)[0] == 2
        
    def test_equality(self):
        assert pair(pair_a) == pair(pair_a)
        
    def test_inequality(self):
        assert not pair(pair_a) == pair(pair_b)
    
    def test_sort(self):
        assert pair(pair_a) > pair(pair_b) > pair(pair_c) > pair(pair_e)

    def test_badSort(self):
        assert not pair(pair_a) < pair(pair_b) < pair(pair_c) < pair(pair_e)

highCard_b = [Card('Hearts',14),Card('Spades',6),Card('Clubs',5),Card('Hearts',3),Card('Diamonds',2)]
highCard_c = [Card('Hearts',14),Card('Hearts',7),Card('Hearts',5),Card('Clubs',3),Card('Diamonds',2)]
highCard_a = [Card('Clubs',13),Card('Diamonds',6),Card('Hearts',4),Card('Spades',3),Card('Hearts',2)]

class TestHighCard:
    def test_bestHand(self):
        assert getBestHand(highCard_a)[0] == 1
        assert getBestHand(highCard_b)[0] == 1
        assert getBestHand(highCard_c)[0] == 1
        
    def test_equality(self):
        assert highCard(highCard_a) == highCard(highCard_a)
    
    def test_inequality(self):
        assert not highCard(highCard_a) == highCard(highCard_b)
        
    def test_sort(self):
        assert highCard(highCard_a) < highCard(highCard_b) < highCard(highCard_c)

    def test_badSort(self):
        assert not highCard(highCard_a) > highCard(highCard_b) > highCard(highCard_c)
        
class TestMostCommonCards:
    def test_order(self):
        c = [Card('Hearts',4),Card('Clubs',4),Card('Spades',6),Card('Diamonds',4),Card('Hearts',2)]
        assert [count for val,count in get_card_value_count(c)] == [3,1,1]