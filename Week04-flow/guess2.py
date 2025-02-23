# Prompts the user to guess a number randomly generated, and tells them if they are correct or not.
# Tells the user if their guess is too high or too low.
# Author: Carmine Giardino

import random

number_to_guess = random.randint(0, 100)
guess = int(input("Please guess the number:"))
while guess != number_to_guess:
    if guess < number_to_guess:
        print("Too low!")
    else:
        print("Too high!")
    guess = int(input("Please guess again:"))
print("Well done! Yes, the number was ", number_to_guess)