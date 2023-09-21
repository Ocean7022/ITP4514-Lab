import random

def getQuestion():
    operator = random.choice(['+', '-', '*', '/'])

    while True:
        firstNum = random.randint(1, 99)
        secondNum = random.randint(1, 99)

        if operator == '/' and (secondNum == 1 or firstNum % secondNum != 0):
            continue
        elif operator == '-' and firstNum < secondNum:
            continue
        else:
            break

    return firstNum, secondNum, operator

def calculateAnswer(firstNum, secondNum, operator):
    if operator == '+':
        return firstNum + secondNum
    elif operator == '-':
        return firstNum - secondNum
    elif operator == '*':
        return firstNum * secondNum
    elif operator == '/':
        return firstNum // secondNum
    
firstNum, secondNum, operator  = getQuestion()

while True:
    playerInput = input(f"Question: {firstNum} {operator} {secondNum} = ? \nYour answer: ")

    try:
        playerInput = int(playerInput)
        break
    except ValueError:
        print("Please input an integer!\n")
        continue

answer = calculateAnswer(firstNum, secondNum, operator)
if playerInput == answer:
    print("Correct!")
else:
    print(f"Incorrect! \nAnswer: {answer}")
