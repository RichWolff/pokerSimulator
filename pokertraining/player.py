from . import Deck
from .checkHands import getBestHand


class Player:
    def __init__(self, name):
        self.name = name
        self.hole = []
        self.bestHandFlop = None
        self.bestHandTurn = None
        self.bestHandRiver = None
        self.win = 0

    def holeCardsCleaned(self):
        cards = ''
        for card in sorted(self.hole, reverse=True):
            if card.value == 10:
                cards += 'T'
            elif card.value == 11:
                cards += 'J'
            elif card.value == 12:
                cards += 'Q'
            elif card.value == 13:
                cards += 'K'
            elif card.value == 14:
                cards += 'A'
            else:
                cards += str(card.value)

        cards += 's' if self.hole[0].suit == self.hole[1].suit else 'o'
        return cards

    def haveNuts(self):
        pass

    def drawCard(self, deck):
        if not isinstance(deck, Deck):
            raise ValueError("Deck not passed to drawCard. Please pass a deck object")
        self.hole.append(deck.drawCard())
        return self

    def showHand(self):
        return self.hole

    def _logHand(self):
        return [str(card) for card in self.hole]

    def clearHand(self):
        self.hole = []
        self.bestHandFlop = None
        self.bestHandTurn = None
        self.bestHandRiver = None
        self.win = 0

    def playerLog(self):
        return ','.join([
            "'"+self.holeCardsCleaned()+"'",
            str(self.bestHandFlop.score),
            str(self.bestHandTurn.score),
            str(self.bestHandRiver.score),
            str(self.win)
        ])

    def __repr__(self):
        return f"Player(name='{self.name}')"

    def __str__(self):
        return f"{self.name}"
