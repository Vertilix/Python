import random
guesses = 0
while True:
    random_number = random.randint(0, 10)
    guesses += 1
    guess = input("What number do you guess? ")
    if guess.isdigit():
       guess = int(guess) 
    else:
       print("Error: Please type in a number")
       continue

    if guess == random_number:
     print("Correct, You got it in", guesses, "guesses")
     break
    else:
        if guess > random_number:
            print("False, You were above the random number")
        else:
            print("False, You were below the random number")