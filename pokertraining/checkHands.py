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

class minimumCardCountError(Exception):
    pass

def getBestHand(cards):
    '''
    Takes a hand of n cards (typically 7 for texas holdem) and iterates through all possible 5 card hands to find the highest hand possible.
    Parameters
    ----------
    cards: list
        list of Card objects to iterate through
    Returns
    --------
    hand object
        the object of the current hand
    Raises
    ------
    minimumCardCountError
        when not enough cards are passed
    '''
    handCheckOrder = [royal_flush, strait_flush, four_of_a_kind, fullHouse, flush, straight, threeOfAKind, twoPair, pair, highCard]
    if len(cards) < 5:
        raise minimumCardCountError(f'Must have at least 5 cards. You passed {len(cards)}.')
    
    allPossibleHands = combinations(cards,5)
    
    # For each possible hand, iterate through each hand, set the hand to each possible hand, started from the best to worst
    # Break when the hand matches the tpye and append to the handOutcomes variable.
    handOutcomes = []
    for hand in allPossibleHands:
        for checkHand in handCheckOrder:
            handType = checkHand(hand)
            if handType._check_hand():
                break
        
        handOutcomes.append(handType)
    
    # Return the highest hand.
    return sorted(handOutcomes,reverse=True)[0]


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
    
    def __str__(self):
        cards = [''.join([cards.suit,str(cards.value)]) for cards in self.cards]
        return ','.join(cards)
    
    def __repr__(self):
        return str(self.cards)


class royal_flush(hand):
    def __init__(self,cards):
        super().__init__(cards)
        self.name = 'Royal Flush'
        self.score = 10

    def _check_hand(self):
        if not (self._is_a_straight() and self._is_flush() and self.mostCommonCards[0][0] == 14):
           return False
        return True
        
    def __eq__(self,other):
        if not self.score == other.score:
            return False
        card1 = self.mostCommonCards[0][0] == other.mostCommonCards[0][0]
        card2 = self.mostCommonCards[1][0] == other.mostCommonCards[1][0]
        card3 = self.mostCommonCards[2][0] == other.mostCommonCards[2][0]
        card4 = self.mostCommonCards[3][0] == other.mostCommonCards[3][0]
        card5 = self.mostCommonCards[4][0] == other.mostCommonCards[4][0]
        
        return card1 and card2 and card3 and card4 and card5
    
    def __lt__(self,other):
        if self.score < other.score:
            return True
        elif self.score == other.score:
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
                         elif self.mostCommonCards[3][0] == other.mostCommonCards[3][0]:
                             if self.mostCommonCards[4][0] < other.mostCommonCards[4][0]:
                                 return True
        return False
    
    def __repr__(self):
        return f'RoyalFlush({self.cards})'
        
class strait_flush(hand):
    def __init__(self,cards):
        super().__init__(cards)
        self.name = 'Strait Flush'
        self.score = 9
        
    def _check_hand(self):
        if not (self._is_a_straight() and self._is_flush()):
           return False
        return True    
    
    def __eq__(self,other):
        if not self.score == other.score:
            return False
        card1 = self.mostCommonCards[0][0] == other.mostCommonCards[0][0]
        card2 = self.mostCommonCards[1][0] == other.mostCommonCards[1][0]
        card3 = self.mostCommonCards[2][0] == other.mostCommonCards[2][0]
        card4 = self.mostCommonCards[3][0] == other.mostCommonCards[3][0]
        card5 = self.mostCommonCards[4][0] == other.mostCommonCards[4][0]
        
        return card1 and card2 and card3 and card4 and card5
    
    def __lt__(self,other):
        if self.score < other.score:
            return True
        elif self.score == other.score:
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
                         elif self.mostCommonCards[3][0] == other.mostCommonCards[3][0]:
                             if self.mostCommonCards[4][0] < other.mostCommonCards[4][0]:
                                 return True
        return False
    def __repr__(self):
        return f'StraightFlush({self.cards})'


class four_of_a_kind(hand):
    def __init__(self, cards):
        super().__init__(cards)
        self.name = 'Four of a Kind'
        self.score = 8
        self.four = self.getFour()
        self.kicker = self.getKicker()

    def getFour(self):
        if self.mostCommonCards[0][1] == 4:
            return self.mostCommonCards[0][0]
        else:
            return False

    def getKicker(self):
        if self.mostCommonCards[1][1] == 1:
            return self.mostCommonCards[1][0]
        else:
            return False

    def _check_hand(self):
        if not ((len(self.mostCommonCards) == 2) and self.mostCommonCards[0][1] == 4 and self.mostCommonCards[1][1] == 1):
            return False
        return True
    
    def __eq__(self, other):
        if not self.score == other.score:
            return False
        return self.mostCommonCards[0][0] == other.mostCommonCards[0][0] and self.mostCommonCards[1][0] == other.mostCommonCards[1][0]
    
    def __lt__(self, other):
        if self.score < other.score:
            return True
        elif self.score == other.score:
            if self.mostCommonCards[0][0] < other.mostCommonCards[0][0]:
                return True
            elif self.mostCommonCards[0][0] == other.mostCommonCards[0][0]:
                if self.mostCommonCards[1][0] < other.mostCommonCards[1][0]:
                    return True
        return False
    def __repr__(self):
        return f'FourOfAKind({self.cards})'
        
class fullHouse(hand):
    def __init__(self,cards):
        super().__init__(cards)
        self.name = 'Full House'
        self.score = 7
        
    def _check_hand(self):
        if not (( len(self.mostCommonCards) == 2) and self.mostCommonCards[0][1] == 3 and self.mostCommonCards[1][1] == 2):
            return False
        return True

    def __eq__(self,other):
        if not self.score == other.score:
            return False
        return self.mostCommonCards[0][0] == other.mostCommonCards[0][0] and self.mostCommonCards[1][0] == other.mostCommonCards[1][0]

    def __lt__(self,other):
        if self.score < other.score:
            return True
        elif self.score == other.score:
            
            if self.mostCommonCards[0][0] < other.mostCommonCards[0][0]:
                return True
            elif self.mostCommonCards[0][0] == other.mostCommonCards[0][0]:
                if self.mostCommonCards[1][0] < other.mostCommonCards[1][0]:
                    return True
        return False
    
    def __repr__(self):
        return f'fullHouse({self.cards})'
        
class flush(hand):
    def __init__(self,cards):
        super().__init__(cards)
        self.name = 'Flush'
        self.score = 6
        
    def _check_hand(self):
        if not self._is_flush():
            return False
        return True
    
    def __eq__(self,other):
        if not self.score == other.score:
            return False
        card1 = self.mostCommonCards[0][0] == other.mostCommonCards[0][0]
        card2 = self.mostCommonCards[1][0] == other.mostCommonCards[1][0]
        card3 = self.mostCommonCards[2][0] == other.mostCommonCards[2][0]
        card4 = self.mostCommonCards[3][0] == other.mostCommonCards[3][0]
        card5 = self.mostCommonCards[4][0] == other.mostCommonCards[4][0]
        
        return card1 and card2 and card3 and card4 and card5
        
    def __lt__(self,other):
        if self.score < other.score:
            return True
        elif self.score == other.score:
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
                         elif self.mostCommonCards[3][0] == other.mostCommonCards[3][0]:
                             if self.mostCommonCards[4][0] < other.mostCommonCards[4][0]:
                                 return True
        return False
    def __repr__(self):
        return f'Flush({self.cards})'
        
class straight(hand):
    def __init__(self,cards):
        super().__init__(cards)
        self.name = 'Straight'
        self.score = 5        
        
    def _check_hand(self):
        if not self._is_a_straight():
            return False
        return True
    
    def __eq__(self,other):
        if not self.score == other.score:
            return False
        
        card1 = self.mostCommonCards[0][0] == other.mostCommonCards[0][0]
        card2 = self.mostCommonCards[1][0] == other.mostCommonCards[1][0]
        card3 = self.mostCommonCards[2][0] == other.mostCommonCards[2][0]
        card4 = self.mostCommonCards[3][0] == other.mostCommonCards[3][0]
        card5 = self.mostCommonCards[4][0] == other.mostCommonCards[4][0]
        
        return card1 and card2 and card3 and card4 and card5
    
    def __lt__(self,other):
        
        if self.score < other.score:
            return True
        
        elif self.score == other.score:
            
            selfScore = self.mostCommonCards[0][0]
            otherScore =  other.mostCommonCards[0][0]
            
            if self.mostCommonCards[0][0] == 14 and self.mostCommonCards[1][0] == 5:
                selfScore = 5
                
            if other.mostCommonCards[0][0] == 14 and other.mostCommonCards[1][0] == 5:
                otherScore = 5
            return selfScore < otherScore
        return False
    def __repr__(self):
        return f'Straight({self.cards})'
            
class threeOfAKind(hand):
    def __init__(self,cards):
        super().__init__(cards)
        self.name = 'Three of a Kind'
        self.score = 4
        self.three = self.mostCommonCards[0][0]
        self.high1 = self.mostCommonCards[1][0]
        self.high2 = self.mostCommonCards[2][0]
        
    def _check_hand(self):
        if not (self.uniqueCardCount == 3 and self.mostCommonCards[0][1] == 3):
            return False
        return True
    
    def __eq__(self,other):
        if not self.score == other.score:
            return False
        return self.three == other.three and self.high1 == other.high1 and self.high2 == other.high2
    
    def __lt__(self,other):
        if self.score < other.score:
            return True
        elif self.score == other.score:
            
            if self.three == other.three:
                if self.high1 == other.high1:
                    if self.high2 < other.high2:
                        return True
                elif self.high1 < other.high1:
                    return True
            elif self.three < other.three:
                return True
        return False
    def __repr__(self):
        return f'ThreeOfAKind({self.cards})'
        
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
        if not (( len(self.mostCommonCards) == 3) and self.mostCommonCards[0][1] == 2 and self.mostCommonCards[1][1] == 2):
            return False
        return True
        
    def __eq__(self,other):
        if not self.score == other.score:
            return False
        return self.pair1 == other.pair1 and self.pair2 == other.pair2 and self.kicker == other.kicker
    
    def __lt__(self,other):
        if self.score < other.score:
            return True
        elif self.score == other.score:
            if self.pair1 == other.pair1:
                if self.pair2 == other.pair2:
                    if self.kicker < other.kicker:
                        return True
                elif self.pair2 < other.pair2:
                    return True
            elif self.pair1 < other.pair1:
                return True
        return False
    def __repr__(self):
        return f'Two Pair({self.cards})'
    
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
        if not(len(self.mostCommonCards) == 4 and self.mostCommonCards[0][1] == 2):
            return False
        return True
            
    def __eq__(self,other):
        if not self.score == other.score:
            return False
        return self.pair == other.pair and self.kicker1 == other.kicker1 and self.kicker2 == other.kicker2 and self.kicker3 == other.kicker3

    def __lt__(self,other):
        if self.score < other.score:
            return True
        elif self.score == other.score:
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
    def __repr__(self):
        return f'Pair({self.cards})'
        
class highCard(hand):
    def __init__(self,cards):
        super().__init__(cards)
        self.name = 'High Card'
        self._check_hand()
        self.score = 1
        self.highCard = self.mostCommonCards[0][0]
        
    def _check_hand(self):
        if self.uniqueCardCount < 5 or self._is_a_straight() or self._is_flush():
            return False
        return True
    
    def __eq__(self,other):
        if not self.score == other.score:
            return False
        card1 = self.mostCommonCards[0][0] == other.mostCommonCards[0][0]
        card2 = self.mostCommonCards[1][0] == other.mostCommonCards[1][0]
        card3 = self.mostCommonCards[2][0] == other.mostCommonCards[2][0]
        card4 = self.mostCommonCards[3][0] == other.mostCommonCards[3][0]
        card5 = self.mostCommonCards[4][0] == other.mostCommonCards[4][0]
        
        return card1 and card2 and card3 and card4 and card5
    
    def __lt__(self,other):
        if self.score < other.score:
            return True
        elif self.score == other.score:
        
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
                         elif self.mostCommonCards[3][0] == other.mostCommonCards[3][0]:
                             if self.mostCommonCards[4][0] < other.mostCommonCards[4][0]:
                                 return True
        return False
    
    def __repr__(self):
        return f'HighCard({self.cards})'
    
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