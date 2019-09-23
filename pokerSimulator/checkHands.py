import numpy as np
import copy
from collections import defaultdict
from collections import Counter
from itertools import combinations
from abc import ABC, abstractmethod

def getCardValues(cards):
    return [c.value for c in sorted(cards)]

def getCardSuits(cards):
    return [c.suit for c in cards]

class WrongHandError(Exception):
    pass
    
class hand(ABC):
    def __init__(self,cards):
        self.cards = sorted(cards,reverse=True)
        self.mostCommonCards = get_card_value_count(cards) 
        self.suitCount = get_card_suit_count(cards) 
        self.uniqueCardCount = len(self.mostCommonCards)
    
    def _is_flush(self):
        return len(self.suitCount) == 1 and self.suitCount[0][1] == 5
    
    def _is_a_straight(self):
        rank_set = set(card.value for card in self.cards)
        rank_range = max(rank_set) - min(rank_set) + 1
        aceHigh = set([2,3,4,5,14])
        return (rank_range == len(self.cards) and len(rank_set) == len(self.cards)) or (rank_set == aceHigh)
    
    @abstractmethod
    def _check_hand(self):
        """Must be a function to ensure the hand is what the class says"""

class royal_flush(hand):
    def __init__(self,cards):
        super().__init__(cards)
        self.name = 'Royal Flush'
        self.score = 10
        self._check_hand()
        
    def _check_hand(self):
        if not (self._is_a_straight() and self._is_flush() and self.mostCommonCards[0][0] == 14):
           raise WrongHandError('Not a Royal Flush')
        
    def __eq__(self):
        return True
        
class four_of_a_kind(hand):
    def __init__(self,cards):
        super().__init__(cards)
        self.name = 'Four of a Kind'
        self.score = 8
        self.four = self.getFour()
        self.kicker = self.getKicker()
        
    def getFour(self):
        if self.mostCommonCards[0][1] == 4:
            return self.mostCommonCards[0][0]
        else:
            raise WrongHandError('Not a 4 of a kind')

    def getKicker(self):
        if self.mostCommonCards[1][1] == 1:
            return self.mostCommonCards[1][0]
        else:
            raise ValueError('Not a 4 of a kind')

    def _check_hand(self):
        pass
            
    def __eq__(self,other):
        return self.four == other.four and self.kicker == other.kicker
    
    def __lt__(self,other):
        if self.four > other.four:
            return False
        if self.four < other.four:
            return True
        if self.four == other.four:
            if self.kicker < other.kicker:
                return True
        return False

class threeOfAKind(hand):
    def __init__(self,cards):
        super().__init__(cards)
        
        self._check_hand()
        
    def _check_hand(self):
        if not self.uniqueCardCount == 3 and self.mostCommonCards[0][1] == 3:
            raise WrongHandError('Not a three of a kind')

class twoPair(hand):
    def __init__(self,cards):
        super().__init__(cards)
        self.name = 'Two Pair'
        self.score = 3
        self.pair1 = self.getPair(0)
        self.pair2 = self.getPair(1)
        self.kicker = self.getPair(2)
        
    def getPair(self,n):
        if len(self.mostCommonCards) == 3:
            return self.mostCommonCards[n][0]
        else:
            return WrongHandError('Not a pair')
        
    def _check_hand(self):
        pass
        
    def __eq__(self,other):
        return self.pair1 == other.pair1 and self.pair2 == other.pair2 and self.kicker == other.kicker
    
    def __lt__(self,other):
        if self.pair1 == other.pair1:
            if self.pair2 == other.pair2:
                if self.kicker < other.kicker:
                    return True
            elif self.pair2 < other.pair2:
                return True
        elif self.pair1 < other.pair1:
            return True
        return False
        
class pair(hand):
    def __init__(self,cards):
        super().__init__(cards)
        self.name = 'Pair'
        self.score = 2
        self._check_hand()
        self.pair = self.getCard(0)
        self.kicker1 = self.getCard(1)
        self.kicker2 = self.getCard(2)
        self.kicker3 = self.getCard(3)

    def getCard(self,loc):
        return self.mostCommonCards[loc][0]

    def _check_hand(self):
        if (not len(self.mostCommonCards) == 4) and self.mostCommonCards[0][1] == 2:
            raise WrongHandError('Not a single pair')          
            
    def __eq__(self,other):
        return self.pair == other.pair and self.kicker1 == other.kicker1 and self.kicker2 == other.kicker2 and self.kicker3 == other.kicker3

    def __lt__(self,other):
        if self.pair < other.pair:
            return True
        if self.pair == other.pair:
            if self.kicker1 < other.kicker1:
                return True
            elif self.kicker1 == other.kicker1 and self.kicker2 < other.kicker2:
                return True
            elif self.kicker1 == other.kicker1 and self.kicker2 == other.kicker2 and self.kicker3 < other.kicker3:
                return True
        return False

class highCard(hand):
        def __init__(self,cards):
            super().__init__(cards)
            self.name = 'High Card'
            print(self.uniqueCardCount)
            self._check_hand()
            self.score = 1
            self.highCard = self.mostCommonCards[0][0]
            
        def _check_hand(self):
            if self.uniqueCardCount < 5 or self._is_a_straight() or self._is_flush():
                raise WrongHandError('Not a high card')
        
        def __eq__(self,other):
            return self.mostCommonCards == other.mostCommonCards
                
        def __lt__(self,other):
            if self.mostCommonCards[0][0] < other.mostCommonCards[0][0]:
                return True
            elif self.mostCommonCards[0][0] == other.mostCommonCards[0][0]:
                if self.mostCommonCards[1][0] < other.mostCommonCards[1][0]:
                    return True
                elif self.mostCommonCards[1][0] == other.mostCommonCards[1][0]:
                    if self.mostCommonCards[2][0] < other.mostCommonCards[2][0]:
                        return True
                    elif self.mostCommonCards[2][0] == other.mostCommonCards[2][0]:
                        if self.mostCommonCards[3][0] < other.mostCommonCards[3][0]:
                            return True
            return False
        


def get_card_value_count(cards):
    tmpCards = getCardValues(cards)
    counter = Counter(tmpCards)
    mostCommonCards = counter.most_common(n=5)
    return sorted(mostCommonCards,key=lambda element: (-element[1],-element[0]))

def get_card_suit_count(cards):
    tmpCards = getCardSuits(cards)
    counter = Counter(tmpCards)
    mostCommonCards = counter.most_common(n=4)
    return sorted(mostCommonCards,key=lambda element: -element[1])
#
#    
#
def check_hands(cards):
    highestHand = 0
    highestCombo = None
    ## Get all 5 hand combinations 
    combos = list(combinations(cards,min(5,len(cards))))
    results = [None]*len(combos)
    for i in combos:
        if is_royal_flush(cards):
            highestHand = 10
            highestHandName = 'Royal Flush'
            highestCombo = i

        elif is_strait_flush(cards) and 9 > highestHand:
            highestHand = 9
            highestHandName = 'Strait Flush'
            highestCombo = i

        elif is_four_of_a_kind(cards) and 8 > highestHand:
            highestHand = 8
            highestHandName = 'Four of a Kind'
            highestCombo = i

        elif is_full_house(cards) and 7 > highestHand:
            highestHand = 7
            highestHandName = 'Full House'
            highestCombo = i

        elif is_flush(cards) and 6 > highestHand:
            highestHand = 6
            highestHandName = 'Flush'
            highestCombo = i

        elif is_strait(cards) and 5 > highestHand:
            highestHand = 5
            highestHandName = 'Strait'
            highestCombo = i

        elif is_three_of_a_kind(cards) and 4 > highestHand:
            highestHand = 4
            highestHandName = 'Three of a Kind'
            highestCombo = i
            
        elif is_two_pair(cards) and 3 > highestHand:
            highestHand = 3
            highestHandName = 'Two Pair'
            highestCombo = i
        
        elif is_pair(cards) and 2 > highestHand:
            highestHand = 2
            highestHandName = 'Pair'
            highestCombo = i
        
        elif 1 > highestHand:
            highestHand = 1
            highestHandName = 'High Card'
            highestCombo = i
            
        return {'Hand Score':highestHand, 'Hand Name':highestHandName,'Card Combo':highestCombo}

def is_royal_flush(cards):
    tmpCards = getCardValues(cards)
    if tmpCards == [10,11,12,13,1] and is_flush(cards): return True

def is_strait_flush(cards):
    return is_flush(cards) and is_strait(cards)

def is_four_of_a_kind(cards):
    mostCommonCards = get_card_value_count(cards)
    if mostCommonCards[0][1] == 4 and mostCommonCards[1][1] == 1:
        return True
    return False

def is_full_house(cards):
    tmpCards = getCardValues(cards)
    res = Counter(tmpCards)
    mostCommonCards = res.most_common(n=5)
    
    if mostCommonCards[0][1] == 3 and mostCommonCards[1][1] == 2:
        return True
    
    return False

def is_flush(cards):
    suits = getCardValues(cards)
    if len(set(suits)) == 1:
        return True
    return False
              
def is_strait(cards):
    tmpCards = getCardValues(cards)
    # Check for ace high strait
    if tmpCards == [2,3,4,5,14]: return True
    
    res = []
    for i,c in enumerate(tmpCards[1:],1):
        res.append(tmpCards[i-1] == tmpCards[i]-1)
    if sum(res) == 4:
        return True
    
    return False

def is_three_of_a_kind(cards):
    tmpCards = getCardValues(cards)
    res = Counter(tmpCards)
    mostCommonCards = res.most_common(n=5)
    if mostCommonCards[0][1] == 3:
        return True
    return False

def is_two_pair(cards):
    tmpCards = getCardValues(cards)
    res = Counter(tmpCards)
    mostCommonCards = res.most_common(n=5)
    if mostCommonCards[0][1] == 2 and mostCommonCards[1][1] == 2:
        return True
    return False

def is_pair(cards):
    mostCommonCards = get_card_value_count(cards)
    if mostCommonCards[0][1] == 2:
        return True
    return False