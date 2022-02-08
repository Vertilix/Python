from time import sleep

print("Simple quiz")

score = 0
playing = input("Would you like to play?")

if playing.lower() == "yes":
    print("Okay")
else:
    quit()

answer = input("Question 1: ")

if answer.lower() =="answer":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

answer = input("Question 2: ")

if answer.lower() =="answer":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

answer = input("Question 3: ")

if answer.lower() =="answer":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

answer = input("Question 4: ")

if answer.lower() =="answer":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

print("You got" + str(score) + "questions right.")
print("You got" + str((score / 4) * 100) + "%.")
sleep(5)



