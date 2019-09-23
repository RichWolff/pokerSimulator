class Card:
    def __init__(self,suit,val):
        
        self.suit = self.checkSuit(suit)
        self.value = val
    
    @staticmethod
    def checkSuit(suit):
        if suit in ('Spades','Hearts','Clubs','Diamonds'):
            return suit
        raise ValueError(f'Suit {suit} not applicable')
        
    def show(self):
        if self.value == 11:
            val = 'Jack'
        elif self.value == 12:
            val = 'Queen'
        elif self.value == 13:
            val = 'King'
        elif self.value == 14:
            val = 'Ace'
        else:
            val = self.value
            
        return self.suit,val
        
    def __repr__(self):
        suit,val = self.show()
        return f"Card(Suit='{suit}',Value='{val}')"
    
    def __str__(self):
        suit,val = self.show()
        return f"{val} of {suit}"    
    def __eq__(self,other):
        return self.value == other.value
    
    def __lt__(self,other): return self.value < other.value
    def __le__(self,other): return self.value <= other.value
    def __ne__(self,other): return self.value != other.value
    def __gt__(self,other): return self.value > other.value
    def __ge__(self,other): return self.value >= other.value