from pokertraining import Deck
from pokertraining.checkHands import getBestHand
import copy
import numpy as np
from collections import deque


class Table:
    def __init__(self, seats):
        self.seats = seats
        self.players = {}
        self.dealerButton = 1
        self.deck = None
        self.flop = []
        self.turn = None
        self.river = None
        self.communityCards = []

    def dealCommunityCards(self, cards):
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
        winners = len(self.players.values()) - maxHandRank

        self.winnerList = [y for x, y in sorted(zip(index, self.players.values()), key=lambda x: -x[0])][:winners]

        numOfWinners = len(self.winnerList)
        for player in self.winnerList:
            player.win = numOfWinners
        return self

    def getBestHands(self, communityPart):
        self.playersBestHands = []
        for player in self.players.values():
            print(player)
            player.bestHand = getBestHand(player.showHand() + self.communityCards) 
            if communityPart.lower() == 'flop':
                player.bestHandFlop = player.bestHand
            elif communityPart.lower() == 'turn':
                player.bestHandTurn = player.bestHand
            elif communityPart.lower() == 'river':
                player.bestHandRiver = player.bestHand
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
        dealorder = deque(self.players.values())
        dealorder.rotate(-self.dealerButton-1)
        for _ in range(2):
            [p.drawCard(self.deck) for p in dealorder]
        return self

    def determineWinner(self, p1, p2=None):
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

    def init_dealer(self):
        deck = Deck()
        deck.shuffle()
        self.dealerButton = self.initDealer_drawing(self.players.keys(), deck)[0]
        return self

    def initDealer_drawing(self, players, deck):
        drawn = {p: deck.drawCard().value for p in players}
        winnerSorted = np.array(sorted(drawn.items(), key=lambda x: x[1], reverse=True))

        results = [True]
        results.extend([pos1[1] == pos2[1] for pos1, pos2 in zip(winnerSorted, winnerSorted[1:])])
        defaultResult = True
        for i, result in enumerate(results):
            if result == 0:
                defaultResult = False
            results[i] = defaultResult

        winners = winnerSorted[results]
        if len(winners) == 1:
            return winners[:, 0]
        else:
            winners = self.initDealer_drawing(winners[:,0], deck)
            return winners

    def addPlayer(self, player):
        if len(self.players) > self.seats:
            raise ValueError('More players than seats')

        if player in self.players.values():
            raise ValueError('Player already at table')

        self.players[len(self.players.keys())] = player

    def __repr__(self):
        return f'Table(Players={list(self.players.values())})'
