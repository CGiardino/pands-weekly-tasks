# Add input numbers in a list and give the average of the numbers when the user enters 0.
# Author: Carmine Giardino

numbers = []
number = int(input("Enter a number (0 to quit): "))
sum = 0
while number != 0:
    numbers.append(number)
    sum += number
    number = int(input("Enter another number (0 to quit): "))
print("The average is", sum / len(numbers))
