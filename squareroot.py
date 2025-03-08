# Program that takes a positive floating-point number as input and outputs an
# approximation of its square root.

# The program uses Newton's method to find the square root of a number.
# Ref: https://patrickwalls.github.io/mathematicalpython/root-finding/newton/
# Ref: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/

# Author: Carmine Giardino


def input_num():
    "Prompts the user to enter a positive floating-point number."
    while True:
        try:
            number = float(input("Please enter a positive number: "))
            if number < 0:
                raise ValueError
            return number
        except ValueError:
            print("Invalid input. Please enter a positive number.")


def sqrt(number):
    "Approximates the square root using Newton's method."
    if number == 0:
        return 0  # Handle the special case where input is 0
    guess = number
    tolerance = 1e-10
    while abs(number - guess**2) > tolerance:
        guess = (guess + number / guess) / 2
    return round(guess, 2)


# Main execution
number = input_num()
print(f"The square root of {number} is {sqrt(number)}")
