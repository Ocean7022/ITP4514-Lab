import random

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
numbers = ['Ace', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', 'Jack', 'Queen', 'King']

while True:
    break
    try:
        playersNum = int(input("How many players? "))
        cardsOfEach = int(input("How many cards for each player? "))

        if playerNum == 0 or cardsOfEach == 0 or playerNum > 52 or cardsOfEach > 52:
            raise ValueError
        elif playerNum * cardsOfEach > 52:
            raise ValueError

        break
    except ValueError:
        print("Incorrect input. Please input again!\n")

cardSet = []
for suit in suits:
    for number in numbers:
        cardSet.append([suit, number])
    cardSet = random.sample(cardSet, len(cardSet))

tmp = []
for index, card in enumerate(cardSet):
    tmp.append([index] + card)
cardSet = tmp

playersHand = []
playersNum = 3
cardsOfEach = 3
for numOfPlayer in range(playersNum):
    redomSet = []
    for card in range(cardsOfEach):
        redomSet.append(cardSet[numOfPlayer + card * playersNum])
    playersHand.append(redomSet)

for player in playersHand:
    print(player)



