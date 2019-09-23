# -*- coding: utf-8 -*-
from .checkHands import pair, twoPair, four_of_a_kind, get_card_value_count
from .card import Card



        
foak_a = four_of_a_kind([Card('Hearts',14),Card('Spades',14),Card('Diamonds',14),Card('Clubs',14),Card('Hearts',10)])
foak_b = four_of_a_kind([Card('Hearts',13),Card('Spades',13),Card('Diamonds',13),Card('Clubs',13),Card('Hearts',10)])
foak_c = four_of_a_kind([Card('Hearts',2),Card('Spades',2),Card('Diamonds',2),Card('Clubs',2),Card('Hearts',14)])



class TestFourOfAKind:
    def test_equality(self):
        assert foak_a == foak_a
        
    def test_sort(self):
        assert foak_a > foak_b
        assert foak_b < foak_a
        assert foak_c < foak_a
        assert foak_c < foak_b
        assert foak_a > foak_c
        
        
twoPair_a = twoPair([Card('Hearts',14),Card('Spades',14),Card('Diamonds',13),Card('Clubs',13),Card('Hearts',5)])
twoPair_b = twoPair([Card('Hearts',13),Card('Spades',13),Card('Diamonds',12),Card('Clubs',12),Card('Hearts',8)])
twoPair_c = twoPair([Card('Hearts',13),Card('Spades',13),Card('Diamonds',12),Card('Clubs',12),Card('Hearts',9)])

class TestTwoPair:
    def test_equality(self):
        assert twoPair_a == twoPair_a
        
    def test_sort(self):
        assert twoPair_a > twoPair_b
        assert twoPair_c > twoPair_b
        
pair_a = pair([Card('Hearts',5),Card('Clubs',5),Card('Spades',10),Card('Diamonds',1),Card('Hearts',3)])
pair_b = pair([Card('Hearts',4),Card('Clubs',4),Card('Spades',14),Card('Diamonds',5),Card('Hearts',3)])
pair_c = pair([Card('Hearts',4),Card('Clubs',4),Card('Spades',6),Card('Diamonds',3),Card('Hearts',2)])
pair_e = pair([Card('Hearts',4),Card('Clubs',4),Card('Spades',6),Card('Diamonds',3),Card('Hearts',1)])

class TestPair:
    def test_equality(self):
        assert pair_a == pair_a
    
    def test_sort(self):
        assert pair_a > pair_b
        assert pair_b > pair_c
        assert pair_c > pair_e
        assert pair_e < pair_a
        assert pair_c < pair_a

highCard_a = [Card('Hearts',4),Card('Clubs',13),Card('Spades',3),Card('Diamonds',6),Card('Hearts',1)]
highCard_b = [Card('Clubs',4),Card('Hearts',14),Card('Hearts',3),Card('Clubs',6),Card('Diamonds',1)]

class TestHighCard:
    def test_equality(self):
        assert highCard_a == highCard_a
    
    def test_sort(self):
        assert highCard_a < highCard_b

class TestMostCommonCards:
    def test_order(self):
        c = [Card('Hearts',4),Card('Clubs',4),Card('Spades',6),Card('Diamonds',4),Card('Hearts',2)]
        assert [count for val,count in get_card_value_count(c)] == [3,1,1]