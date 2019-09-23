
class Table:
    def __init__(self,seats):
        self.seats = seats
        self.players = []
        self.dealerButton = 1
        
    def determineWinner(p1,p2=None):
        if p2 is None:
            return p1
        elif True:
            p1.showHand()
    
    def initDealer(self):
        players = copy.deepcopy(self.players)
        while len(players) > 1:
            deck = Deck()
            deck.shuffle()
            best_card_value = 1
            
            ## First compare player 1 vs player 2
            ## THEN compare player 3 to winner of 1 and 2 (or tie)
            
            for i,p in enumerate(players,1):
                players[i-1].drawCard()
                players[i].drawCard()
                
                winner = 1
            
        best_card = None
        best_player = []
        for player in self.players:
            player.drawCard(deck)
            print(player,player.showHand())
            
            cardValue = player.showHand()[0].value
            card = player.showHand()[0]
            
            if cardValue > best_card_value:
                best_card_value = cardValue
                best_card = card
                best_player = [player]
            
            if cardValue == best_card_value:
                best_player.append(player)
        
        
                
        print(best_player,best_card)
        while len(best_player) > 0:
            deck = Deck()
            deck.shuffle()
            
    def addPlayer(self,player):
        if len(self.players) > self.seats:
            raise ValueError('More players than seats')
            
        if player in self.players:
            raise ValueError('Player already at table')
            
        self.players.append(player)
    
    def __repr__(self):
        return f'Table(Players={self.players})'