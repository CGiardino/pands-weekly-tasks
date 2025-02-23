# Prompts the user to guess a number, and tells them if they are correct or not.
# Author: Carmine Giardino

number_to_guess = 30
guess = int(input("Please guess the number:"))
while guess != number_to_guess:
    print("Wrong!")
    guess = int(input("Please guess again:"))
print("Well done! Yes, the number was ", number_to_guess)