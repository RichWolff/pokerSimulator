# -*- coding: utf-8 -*-

from pokertraining import Deck, Player, Table
from pokertraining.checkHands import getBestHand
from collections import Counter
import time
import uuid

def outsideStraightDraw(cards):
    outsideDraw = 0
    insideStraightDraw = 0
    doubleInsideStraitDraw = 0
    cards = sorted(cards,reverse=True)
    values = [card.value for card in cards] 
    valMath = [0]*(len(values)-1)

    # get distance between cards
    for i,val in enumerate(values):
        if i == 4: break
        valMath[i] = values[i]-values[i+1]
    
    # check if outside draw exists
    if not valMath == [1,1,1,1]:
        if ((valMath[1:] == [1,1,1]) and values[1] >= 2 and values[3] <= 13 ) or\
            ((valMath[:3] == [1,1,1]) and values[0] >= 2 and values[2] <= 13): 
            outsideDraw = 1
    
    # check if double inside strait draw exists
    # 2,1,1,2 is normal, 7,2,1,1 show a,3,4,5,7 draw
    if valMath == [2,1,1,2] or valMath == [7,2,1,1]:
        doubleInsideStraitDraw = 1
    
    # TODO design inside straight draw
    # Check for inside straight draw
    # if draw is a,2,3,4
    # ace to 5 inside straight draws
    a5draws = [[14,5,4,3],[14,5,3,2],[14,4,3,2],[14,5,4,2]]
    if ([values[0]]+values[2:] in a5draws) and (not values[1] == 5): insideStraightDraw = 1
    if values[:4] == [14,13,12,11]: insideStraightDraw = 1
        
    return [outsideDraw,doubleInsideStraitDraw,insideStraightDraw]


tbl = Table(seats=9)
for p in range(9):
    tbl.addPlayer(Player(f'{p}'))

handID = uuid.uuid4().hex

tbl.getDeckAndShuffle()
tbl.dealHoleCards()

tbl.burnCard()
tbl.dealCommunityCards('flop')
tbl.getBestHands('flop')

tbl.burnCard()
tbl.dealCommunityCards('turn')
tbl.getBestHands('turn')

tbl.burnCard()
tbl.dealCommunityCards('river')
tbl.getBestHands('river')

tbl.getWinners()

    
print(tbl.winnerList)
#print(tbl.playersBestHands)
print('handId,holeCardGroup,holeCards,Flop,Turn,River,flush_draw,outside_straight_draw,double_inside_straight_draw,bestHandFlop,bestHandTurn,bestHandRiver,Win')
for player in tbl.players:
    flopHand = player.showHand() + tbl.flop
    suits = Counter([card.suit for card in flopHand])
    flushDraw = 1 if 5 not in suits.values() and 4 in suits.values() else 0
    straightDraws = outsideStraightDraw(flopHand)
    print(
            ','.join([
                handID,                    
                str(player.holeCardsCleaned()), 
                '|'.join(player._logHand()), 
                '|'.join(tbl._logFlop()), 
                tbl._logTurn(), 
                tbl._logRiver(),
                str(flushDraw),
                ','.join([str(draw) for draw in straightDraws]),
                str(player.bestHandFlop.score),
                str(player.bestHandTurn.score),
                str(player.bestHandRiver.score),
                str(player.win),
            ])
    )
#    for i,player in enumerate(players):
#        if previousBest is None:
#            winner = i
#            previousBest = player.bestHandRiver
#        else:
#            best = player.bestHandRiver
#            if best > previousBest:
#                previousBest = best
#                winner = i
#                
#    players[winner].win = 1
#    
#    
#    for player in players: 
#        with open('handLog.txt','a') as file:
#            file.write(player.playerLog()+'\n')
