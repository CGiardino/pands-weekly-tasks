# Prints out all the even numbers from 2 to 100
# Author Carmine Giardino

number_to = 100
for i in range(2, number_to + 1):
    if i % 2 == 0:
        print(i, end=" ")
