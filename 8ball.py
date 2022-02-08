import random

answers = ["yes", "maybe", "no"]

while True:
    userInput = input("Ask a question: ")
    ballPick = answers[random.randint(0,2)]
    if userInput:
        print(ballPick)
    else:
        print("Please ask a question")