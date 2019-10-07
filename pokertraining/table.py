from pokertraining import Deck
from pokertraining.checkHands import getBestHand


class Table:
    def __init__(self,seats):
        self.seats = seats
        self.players = []
        self.dealerButton = 1
        self.flop = []
        self.turn = None
        self.river = None
        self.communityCards = []
      
    def dealCommunityCards(self,cards):
        if cards.lower() == 'flop':
            self.flop.extend([self.deck.drawCard() for _ in range(3)])
            self.communityCards.extend(self.flop)
            
        elif cards.lower() == 'turn':
            self.turn = self.deck.drawCard()
            self.communityCards.append(self.turn)
            
        elif cards.lower() == 'river':
            self.river = self.deck.drawCard()
            self.communityCards.append(self.river)
        return self
    
    def getWinners(self):
        seq = sorted(self.playersBestHands)
        index = [seq.index(v) for v in self.playersBestHands]
        maxHandRank = max(index)
        winners = len(self.players) - maxHandRank
        
        self.winnerList = [y for x,y in sorted(zip(index,self.players),key=lambda x: -x[0])][:winners]
        
        numOfWinners = len(self.winnerList)
        for player in self.winnerList:
            player.win = numOfWinners
        return self
        
            
    def getBestHands(self,communityPart):
        self.playersBestHands = []
        for player in self.players:
            player.bestHand = getBestHand(player.showHand() + self.communityCards) 
            if communityPart.lower() == 'flop': player.bestHandFlop = player.bestHand
            elif communityPart.lower() == 'turn': player.bestHandTurn = player.bestHand
            elif communityPart.lower() == 'river': player.bestHandRiver = player.bestHand
            self.playersBestHands.append(player.bestHand)
        return self
    
    def clearCommunityCards(self):
        self.flop = []
        self.turn = None
        self.river = None
        self.communityCards = []
        return self
    
    def burnCard(self):
        self.deck.drawCard()
        return self
    
    def getDeckAndShuffle(self):
        self.deck = Deck()
        self.deck.shuffle()
        return self
        
    def dealHoleCards(self):
        for _ in range(2):
            for player in self.players:
                player.drawCard(self.deck)
        return self
       
    def determineWinner(p1,p2=None):
        if p2 is None:
            return p1
        elif True:
            p1.showHand()
            
    def _logFlop(self):
        return [str(card) for card in self.flop]
 
    def _logTurn(self):
        return str(self.turn)
    
    def _logRiver(self):
        return str(self.river)
                   
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