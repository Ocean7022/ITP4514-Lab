import random

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
numbers = ['Ace', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

while True:
    try:
        playersNum = int(input("How many players? "))
        cardsOfEach = int(input("How many cards for each player? "))

        if playersNum == 0 or cardsOfEach == 0 or playersNum > 52 or cardsOfEach > 52:
            raise ValueError
        elif playersNum * cardsOfEach > 52:
            raise ValueError

        break
    except ValueError:
        print("Incorrect input. Please input again!\n")

cardSet = []
for suit in suits:
    for number in numbers:
        cardSet.append([suit, number])
    cardSet = random.sample(cardSet, len(cardSet))

playersHand = []
for numOfPlayer in range(playersNum):
    redomSet = []
    for card in range(cardsOfEach):
        redomSet.append(cardSet[numOfPlayer + card * playersNum])
    playersHand.append(redomSet)

for playerCards in playersHand:
    print(f"Player {playersHand.index(playerCards) + 1}'s hand:")
    print("    suit     number")
    
    for card in playerCards:
        print(f"{playerCards.index(card):<3} {card[0]:<9} {card[1]:>5}")


