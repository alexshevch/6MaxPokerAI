cardSuits = ["c", "d", "h", "s"]
cardValues = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
cardValuesStr = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
pos = ["SB","BB","EP","MP","CO","BU"]
combinations = ["High Card", "1 Pair", "2 Pairs", "3 Of a Kind", "Straight",
                "Flush", "Full House", "4 Of A Kind", "Straight Flush"]

ranges = [["AA","KK","QQ"],["AKs", "AKo"],["JJ","TT", "99"],["AQs","AQo","AJs","AJo","ATs","ATo"],
          ["88","77","66"],["A9s","A8s","A7s","A6s","A5s","A4s","A3s","A2s"],
          ["KQs","KJs","KTs","QJs","QTs","JTs"],["KQo","KJo","KTo","QJo","QTo","JTo"],
          ["55","44","33","22"],["T9s","98s","87s","76s","65s","54s","43s","32s"]]
stealRange = ["A9o","A8o","A7o","A6o","A5o","A4o","A3o","A2o","K9s","K8s","K7s","Q9s","Q8s","Q9o","J9s"]

def generateDeck():
    deck = []
    for suit in cardSuits:
        for value in cardValues:
            deck.append((value,suit))
    return deck
