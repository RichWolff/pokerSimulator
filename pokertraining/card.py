class Card:
    def __init__(self,suit,val):
        
        self.suit = self.checkSuit(suit)
        self.value = self.checkValue(val)
    
    @staticmethod
    def checkSuit(suit):
        if suit in ('Spades','Hearts','Clubs','Diamonds'):
            return suit
        raise ValueError(f'Suit {suit} not applicable')
        
    @staticmethod 
    def checkValue(val):
        if val < 2 or val > 14:
            raise ValueError(f'Card {val} is not valid. Must be a numerical integer between 2 and 14)')
        return val
    
    def show(self):
        if self.value == 11:
            val = 'J'
        elif self.value == 12:
            val = 'Q'
        elif self.value == 13:
            val = 'K'
        elif self.value == 14:
            val = 'A'
        else:
            val = str(self.value)
        
        suits_symbols = {'Spades':'♠', 'Diamonds':'♦', 'Hearts':'♥', 'Clubs':'♣'}
        return str(val + suits_symbols[self.suit])
    
    def __repr__(self):
        return str(self.show())
    
    def __str__(self):
        return str(self.show())
    
    
    def __eq__(self,other):
        return self.value == other.value
    
    def __lt__(self,other): return self.value < other.value
    def __le__(self,other): return self.value <= other.value
    def __ne__(self,other): return self.value != other.value
    def __gt__(self,other): return self.value > other.value
    def __ge__(self,other): return self.value >= other.value