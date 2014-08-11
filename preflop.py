from random import randint
import defs


# activePlayers is a list of players remaining ingame
# each player has [name, stack, position, bets history, stats(later)]
# sorted by position: sb = activePlayers[0], button = activePlayers[5]
activePlayers = []


def preflop(sb,bb):
    deck = defs.generateDeck()
    heroPos = randint(0,5) # get hero's position
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
            if EPbet == bb:
                oneLimper(rangeIndex, heroPos, bb)
            elif EPbet == 0:
                foldEP(rangeIndex, heroPos, bb)
            elif EPbet > 4*bb:
                openPush(rangeIndex, heroPos, bb)
            else: #EPbet <= 4bb
                raiseMP(rangeIndex, heroPos, bb)
#^^^^^structured^^^^^
#vvvvv unstructured vvvvvv
    elif heroPos == 4:
            EPbet = int(raw_input("EP: "))
            activePlayers[2][3].append(EPbet)
            #EP bet evaluation
            MPbet = int(raw_input("MP: "))
            activePlayers[3][3].append(MPbet)
            #MP bet evaluation
    elif heroPos == 5:
            EPbet = int(raw_input("EP: "))
            activePlayers[2][3].append(EPbet)
            #EP bet evaluation
            MPbet = int(raw_input("MP: "))
            activePlayers[3][3].append(MPbet)
            #MP bet evaluation
            #....            
            CObet = int(raw_input("CO: "))
            activePlayers[4][3].append(MPbet)
            #CO bet evaluation

    print activePlayers

#preflop single action functions

def foldEP(rangeIndex, heroPos, bb):
    if rangeIndex > 7:
        activePlayers[heroPos][3].append(bb)
        print activePlayers[heroPos][0]+": "+str(bb)
        # process next player
    else:
        activePlayers[heroPos][3].append(3*bb)
        print activePlayers[heroPos][0]+": "+str(3*bb)
        # process next player

def oneLimper(rangeIndex, heroPos, bb):
    if rangeIndex > 7:
        activePlayers[heroPos][3].append(bb)
        print activePlayers[heroPos][0]+": "+str(bb)
        # process next player
    else:
        activePlayers[heroPos][3].append(3*bb)
        print activePlayers[heroPos][0]+": "+str(3*bb)
        # process next player

def openPush(rangeIndex, heroPos, bb):
    if rangeIndex > 1:
        activePlayers[heroPos][3].append(0)
        print activePlayers[heroPos][0]+": "+str(0)
        #done
    else:
        activePlayers[heroPos][3].append(activePlayers[heroPos][2])
        print activePlayers[heroPos][0]+": "+str(activePlayers[heroPos][2]) 
        # process next player

def raiseMP(rangeIndex, heroPos, bb):
    if rangeIndex > 1:
        activePlayers[heroPos][3].append(EPbet)
        print activePlayers[heroPos][0]+": "+str(EPbet)
        # process next player
    else:
        activePlayers[heroPos][3].append(3*EPbet)
        print activePlayers[heroPos][0]+": "+str(3*EPbet)
        # process next player

preflop(1, 2)


