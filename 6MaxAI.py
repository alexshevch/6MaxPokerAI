from random import randint
import preflop
import defs



def evalHand(cards):
    # returns evalResult - integer, strength of combination, 
    #         values - list of occurences by values
    evalResult = 0
    values = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    for card in cards:
        values[int(card[0])-2] += 1
    maxValue = max(values)
    maxIndex = values.index(maxValue)
    if maxValue == 4:
        evalResult = 7
    elif maxValue == 3:
        if 2 in values:
            evalResult = 6
        else:
            evalResult = 3
    elif maxValue == 2:
        #maxInvertedValue = values.values()[::-1]
        #maxInvertedIndex = 14 - invertedCount.index(maxInvertedValues)
        if values.count(2) == 2:
            evalResult = 2
        else:
            evalResult = 1
    else:
        flush = False
        # Order: clubs = 1, diamonds = 2, hearts = 3, spades = 4
        suits = [0,0,0,0]
        for card in cards: 
            suits[card[1]-1] += 1
        if max(suits) == 5:
            flush = True
        minIndex = maxIndex
        maxIndex = max(values[::-1])
        if maxIndex - minIndex == 5:
            if flush == True:
                evalResult = 8
            else:
                evalResult = 4
        elif flush == True:
             evalResult = 5
        else:
             evalResult = 0
    return evalResult, values

def compareHands():
    player1Win = 0
    f = open("poker.txt", "r")
    for line in f:
        cards = line.split(" ", 10)
        cards[9] = cards[9].replace("\n", "")
        for i in range(10):
            cards[i] = list(cards[i])
            if cards[i][0] == 'T':
                cards[i][0] = '10'
            if cards[i][0] == 'J':
                cards[i][0] = '11'
            if cards[i][0] == 'Q':
                cards[i][0] = '12'
            if cards[i][0] == 'K':
                cards[i][0] = '13'
            if cards[i][0] == 'A':
                cards[i][0] = '14'

            if cards[i][1] == 'C':
                cards[i][1] = '1'
            if cards[i][1] == 'D':
                cards[i][1] = '2'
            if cards[i][1] == 'H':
                cards[i][1] = '3'
            if cards[i][1] == 'S':
                cards[i][1] = '4'
            #cards[i][0] = int(cards[i][0])
            cards[i][1] = int(cards[i][1])


        evalResult1, evalResult2 = evalHand(cards[:5]), evalHand(cards[5:])
        if evalResult1[0] > evalResult2[0]:
            player1Win = player1Win + 1
        else:
            if evalResult1[0] == evalResult2[0]:
                tempList = [3, 4, 6, 7, 8]
                if evalResult1[0] in tempList:
                    maxIndex1 = evalResult1[1].index(max(evalResult1[1]))
                    maxIndex2 = evalResult2[1].index(max(evalResult2[1]))
                    if maxIndex1 > maxIndex2:
                        player1Win = player1Win + 1
                elif evalResult1[0] == 5 or evalResult1[0] == 0:
                    list1, list2 = [], [] 
                    for i in range(13):
                        if evalResult1[1][i] == 1:
                            list1.append(i+2)
                        if evalResult2[1][i] == 1:
                            list2.append(i+2)
                    list1 = sorted(list1, reverse=True)
                    list2 = sorted(list2, reverse=True)
                    for i in range(5):
                        if list1[i] > list2[i]:
                            player1Win = player1Win + 1
                            break
                        elif list1[i] < list2[i]:
                            break
                        
                elif evalResult1[0] == 2:
                    minIndex1 = evalResult1[1].index(max(evalResult1[1]))
                    minIndex2 = evalResult2[1].index(max(evalResult2[1]))
                    maxIndex1 = evalResult1[1].index(max(evalResult1[1][::-1]))
                    maxIndex2 = evalResult2[1].index(max(evalResult2[1][::-1]))
                    print minIndex1, minIndex2, maxIndex1, maxIndex2
                    if maxIndex1 > maxIndex2:
                        player1Win = player1Win + 1
                    elif maxIndex1 == maxIndex2:
                        if minIndex1 > minIndex2:
                            player1Win = player1Win + 1

                else:
                    #evalResult1[0] = 1
                    maxIndex1 = evalResult1[1].index(max(evalResult1[1]))
                    maxIndex2 = evalResult2[1].index(max(evalResult2[1]))
                    if maxIndex1 > maxIndex2:
                        player1Win = player1Win + 1
                    elif maxIndex1 == maxIndex2:
                        list1, list2 = [], [] 
                        for i in range(13):
                            if evalResult1[1][i] == 1:
                                list1.append(i+2)
                            if evalResult2[1][i] == 1:
                                list2.append(i+2)
                        list1 = sorted(list1, reverse=True)
                        list2 = sorted(list2, reverse=True)
                        for i in range(5):
                            if list1[i] > list2[i]:
                                player1Win = player1Win + 1
                                break
                            elif list1[i] < list2[i]:
                                break

    print player1Win

preflop(1, 2)


