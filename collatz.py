# Collatz problem: user input any positive integer and outputs the successive
# values of the following calculation:
# At each step, if the current value is even, the next value is the current
# value divided by two.
# If the current value is odd, the next value is the current value multiplied
# by three plus one.
# The sequence ends if the current value is one.

# Author: Carmine Giardino

input_to_parse = input("Enter a positive integer: ")
while (not input_to_parse.isdigit()) or (int(input_to_parse) <= 0):
    input_to_parse = input("Please enter a positive integer: ")

number = int(input_to_parse)
print(number, end=" ")
while number != 1:
    if number % 2 == 0:
        number = int(number / 2)
    else:
        number = int(number * 3 + 1)
    print(number, end=" ")
print()
