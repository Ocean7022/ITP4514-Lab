import random

answer = random.randint(1, 100)
print(answer)

steps = 0
minNum = 1
maxNum = 100

while steps < 99:
    steps += 1
    userInput = int(input(f"Step {steps}\nPlease guess the answer between {minNum} to {maxNum}: "))

    if userInput == answer:
        print(f"You win! You used {steps} steps to guess the answer!")
        break
    elif userInput < answer:
        print("Your answer is too small!")
        minNum = max(minNum, userInput)
    else:
        print("Your answer is too large!")
        maxNum = min(maxNum, userInput)

    print(f"The range should be between {minNum} to {maxNum}")