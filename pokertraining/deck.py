import numpy as np
from . import Card

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        for s in ['Spades','Clubs','Diamonds','Hearts']:
            for v in range(2,15):
                self.cards.append(Card(s,v))
                
    def showCards(self):
        return [print(card) for card in self.cards]

    def __repr__(self):
        return str([card for card in self.cards])
    
    def shuffle(self):
        self.cards = list(np.random.permutation(self.cards))
            
    def drawCard(self):
        return self.cards.pop()