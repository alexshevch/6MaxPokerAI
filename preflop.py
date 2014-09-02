from random import randint
import defs
import sys


# activePlayers is a list of players remaining ingame
# each player has [name, stack, position, bets history, stats(later)]
# sorted by position: sb = activePlayers[0], button = activePlayers[5]
activePlayers = []


def preflop(sb,bb):
    deck = defs.generateDeck()
    heroPos = int(raw_input("hero pos from 0 to 5: "))
    myCards = ((10,"h"),(11,"s"))
    deck.remove(myCards[0])
    deck.remove(myCards[1])
    #print deck

    for i in range(0,6):
        activePlayers.append([defs.pos[i], i, randint(150*sb,250*sb), []])

    activePlayers[heroPos][0] = "ua-slalom"
    activePlayers[0][3].append(sb)
    print activePlayers[0][0]+": "+str(sb)
    activePlayers[1][3].append(bb)
    print activePlayers[1][0]+": "+str(bb)

    card1 = defs.cardValuesStr[myCards[0][0]-2]
    card2 = defs.cardValuesStr[myCards[1][0]-2]

    myHand = defs.cardValuesStr[max(myCards[0][0], myCards[1][0])-2] + defs.cardValuesStr[min(myCards[0][0], myCards[1][0])-2]
    if myCards[0][0] != myCards[1][0]:
        if myCards[0][1] == myCards[1][1]:
            myHand = myHand + "s"
        else:
            myHand = myHand + "o"
    print myHand

    # determine range for hero's hand
    rangeIndex = 0
    for Range in defs.ranges:
        if myHand in Range:
            break
        rangeIndex += 1
    print rangeIndex
    if rangeIndex == 10:
        activePlayers[heroPos][3].append(0)
        print activePlayers[heroPos][0]+": "+str(0)
        #done
    if heroPos == 2:
        foldEP(rangeIndex, heroPos, bb)
    elif heroPos == 3:
        EPbet = int(raw_input("EP: "))
        activePlayers[2][3].append(EPbet)
        if EPbet == 0:
            foldEP(rangeIndex, heroPos, bb)
        elif EPbet == bb:
            limperLP(rangeIndex, heroPos, bb)
        elif EPbet <= 4*bb:
            raiseLP(rangeIndex, heroPos, bb)
        else: #EPbet > 4bb
            openPush(rangeIndex, heroPos, bb)
    elif heroPos == 4:
        EPbet = int(raw_input("EP: "))
        activePlayers[2][3].append(EPbet)
        MPbet = int(raw_input("MP: "))
        activePlayers[3][3].append(MPbet)
        if EPbet == 0:
            if MPbet == 0:
                foldEP(rangeIndex, heroPos, bb)
            elif MPbet == bb:
                limperLP(rangeIndex, heroPos, bb)
            elif MPbet <= 4*bb:
                raiseLP(rangeIndex, heroPos, bb)
            else: #MPbet > 4bb
                openPush(rangeIndex, heroPos, bb)
        elif EPbet == bb:
            if MPbet <= bb:
                limperLP(rangeIndex, heroPos, bb)
            elif MPbet <= 4*bb:
                raiseLP(rangeIndex, heroPos, bb)
            else: #MPbet > 4bb
                openPush(rangeIndex, heroPos, bb)
        elif EPbet <= 4*bb:
            if MPbet == 0:
                raiseLP(rangeIndex, heroPos, bb)
            elif MPbet <= 4*bb:
                raiseCall(rangeIndex, heroPos, bb)
            else: #MPbet > 4bb
                openPush(rangeIndex, heroPos, bb)
        else: #EPbet > 4bb
            if MPbet == 0:
                openPush(rangeIndex, heroPos, bb)
            else:
                reRase(rangeIndex, heroPos, bb)
    elif heroPos == 5:
        EPbet = int(raw_input("EP: "))
        activePlayers[2][3].append(EPbet)
        MPbet = int(raw_input("MP: "))
        activePlayers[3][3].append(MPbet)           
        LPbet = int(raw_input("CO: ")) 
        activePlayers[4][3].append(LPbet)
        if EPbet == 0:
            if MPbet == 0:
                if LPbet == 0:
                    foldEP(rangeIndex, heroPos, bb)
                elif LPbet == bb:
                    limperLP(rangeIndex, heroPos, bb)
                elif LPbet <= 4*bb:
                    raiseLP(rangeIndex, heroPos, bb)
                else: #LPbet > 4bb
                    openPush(rangeIndex, heroPos, bb)
            elif MPbet <= 4*bb:
                if LPbet == 0:
                    raiseLP(rangeIndex, heroPos, bb)
                elif LPbet <= 4*bb:
                    raiseCall(rangeIndex, heroPos, bb)
                else: #LPbet > 4bb
                    reRaise(rangeIndex, heroPos, bb)
            else: #MPbet > 4bb
                if LPbet == 0:
                    openPush(rangeIndex, heroPos, bb)
                else:
                    reRaise(rangeIndex, heroPos, bb)
        elif EPbet == bb:
            if MPbet <= bb:
                if LPbet <= bb:
                    limperLP(rangeIndex, heroPos, bb)
                elif LPbet <= 4*bb:
                    raiseLP(rangeIndex, heroPos, bb)
                else: #LPbet > 4bb
                    openPush(rangeIndex, heroPos, bb)
            elif MPbet <= 4*bb:
                if LPbet == 0:
                    raiseLP(rangeIndex, heroPos, bb)
                elif LPbet <= 4*bb:
                    raiseCall(rangeIndex, heroPos, bb)
                else: #LPbet > 4bb
                    reRaise(rangeIndex, heroPos, bb)
            else: #MPbet > 4bb
                if LPbet == 0:
                    openPush(rangeIndex, heroPos, bb)
                else:
                    reRaise(rangeIndex, heroPos, bb)
        elif EPbet <= 4*bb:
            if MPbet == 0:
                if LPbet == 0:
                    raiseLP(rangeIndex, heroPos, bb)
                elif LPbet <= 4*bb:
                    raiseCall(rangeIndex, heroPos, bb)
                else: #LPbet > 4bb
                    reRaise(rangeIndex, heroPos, bb)
            elif MPbet <= 4*bb:
                if LPbet <= 4*bb:
                    raiseCall(rangeIndex, heroPos, bb)
                else: #LPbet > 4bb
                    reRaise(rangeIndex, heroPos, bb)
            else: #MPbet > 4bb
                reRase(rangeIndex, heroPos, bb)
        else: #EPbet > 4bb
            if MPbet == 0 and LPbet == 0:
                openPush(rangeIndex, heroPos, bb)
            else:
                reRaise(rangeIndex, heroPos, bb)
    else:
        EPbet = int(raw_input("EP: "))
        activePlayers[2][3].append(EPbet)
        MPbet = int(raw_input("MP: "))
        activePlayers[3][3].append(MPbet)           
        LPbet = int(raw_input("CO: ")) 
        activePlayers[4][3].append(LPbet)
        BUbet = int(raw_input("BU: ")) 
        activePlayers[5][3].append(BUbet)
        maxBet = max(EPbet,MPbet,LPbet,BUbet)
        sumBet = sum(EPbet,MPbet,LPbet,BUbet)
        print maxBet
        if maxBet == 0:
            foldSBB(rangeIndex, heroPos, bb)
        elif maxBet == bb:
            limperSBB(rangeIndex, heroPos, bb)
        elif maxBet <= 4*bb:
            if sumBet <= 4*bb:
                raiseSBB(rangeIndex, heroPos, bb)
            else sumbet <= 6*bb:
                raiseCall(rangeIndex, heroPos, bb)
        else: #maxBet > 4*bb
            if sumBet == maxBet:
                openPush(rangeIndex, heroPos, bb)
            else:
                reRaise(rangeIndex, heroPos, bb)

    #print activePlayers

#preflop single action functions

def foldEP(rangeIndex, heroPos, bb):
    """
    Abstractions for position actions:
     - opponents' actions: everyone folds
     - hero's position: EP/MP 
    """
    action = sys._getframe().f_code.co_name
    print str(action)

    if rangeIndex > 7:
        activePlayers[heroPos][3].append(bb)
        print activePlayers[heroPos][0]+": "+str(bb)
        # process next player
    else:
        activePlayers[heroPos][3].append(3*bb)
        print activePlayers[heroPos][0]+": "+str(3*bb)
        # process next player

def limperLP(rangeIndex, heroPos, bb):
    """
    Abstractions for position actions:
     - opponents' actions: limper(s)
     - hero's position: MP/CO/BU
    """
    action = sys._getframe().f_code.co_name
    print str(action)

    if rangeIndex > 7:
        activePlayers[heroPos][3].append(bb)
        print activePlayers[heroPos][0]+": "+str(bb)
        # process next player
    else:
        activePlayers[heroPos][3].append(3*bb)
        print activePlayers[heroPos][0]+": "+str(3*bb)
        # process next player

def openPush(rangeIndex, heroPos, bb):
    """
    Abstractions for position actions:
     - opponents' actions: push
     - hero's position: MP/CO/BU/SB/BB 
    """
    action = sys._getframe().f_code.co_name
    print str(action)

    if rangeIndex > 1:
        activePlayers[heroPos][3].append(0)
        print activePlayers[heroPos][0]+": "+str(0)
        #done
    else:
        activePlayers[heroPos][3].append(activePlayers[heroPos][2])
        print activePlayers[heroPos][0]+": "+str(activePlayers[heroPos][2]) 
        # process next player

def raiseLP(rangeIndex, heroPos, bb):
    """
    Abstractions for position actions:
     - opponents' actions: one raise
     - hero's position: MP/CO/BU
    """
    action = sys._getframe().f_code.co_name
    print str(action)

    if rangeIndex > 1:
        activePlayers[heroPos][3].append(EPbet)
        print activePlayers[heroPos][0]+": "+str(EPbet)
        # process next player
    else:
        activePlayers[heroPos][3].append(3*EPbet)
        print activePlayers[heroPos][0]+": "+str(3*EPbet)
        # process next player

def foldLP(rangeIndex, heroPos, bb):
    """
    Abstractions for position actions:
     - opponents' actions: everyone folds
     - hero's position: CO/BU
    """
    action = sys._getframe().f_code.co_name
    print str(action)

    return rangeIndex

def foldSBB(rangeIndex, heroPos, bb):
    """
    Abstractions for position actions:
     - opponents' actions: everyone folds
     - hero's position: SB/BB
    """
    action = sys._getframe().f_code.co_name
    print str(action)

    return rangeIndex

def limperSBB(rangeIndex, heroPos, bb):
    """
    Abstractions for position actions:
     - opponents' actions: limper(s)
     - hero's position: SB/BB
    """
    action = sys._getframe().f_code.co_name
    print str(action)

    return rangeIndex

def raiseSBB(rangeIndex, heroPos, bb):
    """
    Abstractions for position actions:
     - opponents' actions: one raise
     - hero's position: SB/BB
    """
    action = sys._getframe().f_code.co_name
    print "raiseSBB"
    return rangeIndex

def raiseCall(rangeIndex, heroPos, bb):
    """
    Abstractions for position actions:
     - opponents' actions: raise + call(s)
     - hero's position: CO/BU/SB/BB
    """
    action = sys._getframe().f_code.co_name
    print str(action)

    return rangeIndex

def reRaise(rangeIndex, heroPos, bb):
    """
    Abstractions for position actions:
     - opponents' actions: raise + reraise
     - hero's position: CO/BU/SB/BB
    """
    action = sys._getframe().f_code.co_name
    print str(action)

    return rangeIndex

preflop(1, 2)


