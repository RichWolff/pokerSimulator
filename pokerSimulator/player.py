from . import Deck
from .checkHands import check_hands

class Player:
    def __init__(self,name):
        self.name = name
        self.hand = []
        self.bestHand = None

    def drawCard(self,deck):
        if not isinstance(deck,Deck):
            raise ValueError("Deck not passed to drawCard. Please pass a deck object")
        self.hand.append(deck.drawCard())
        return self
    
    def showHand(self):
        return self.hand
    
    def clearHand(self):
        self.hand = []
        
    def getBestHand(self):
        self.bestHand = check_hands(self.showHand())
        return self.bestHand['Hand Name'], self.bestHand['Card Combo']

    def __repr__(self):
        return f"Player(name='{self.name}')"
    
    def __str__(self):
        return f"{self.name}"
