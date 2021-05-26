import random


random_number = random.randint(1, 100)
users_guess = input("Guess a number from 1 - 100 : ")
guess_count = 0
guessed_right = False

while not guessed_right:
    guess_count += 1
    if int(users_guess) == random_number:
        print("It took " + str(guess_count) + " guesses")
        guessed_right = True
    elif int(users_guess) > random_number:
        print("Guess lower")
        users_guess = input("Please try again: ")  # updates users guess
        guessed_right = False
    elif int(users_guess) < random_number:
        print("Guess guess higher")
        users_guess = input("Please try again: ")
