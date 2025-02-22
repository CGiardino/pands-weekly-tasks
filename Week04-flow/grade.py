# Reads a student's score and prints the corresponding grade.
# Author: Carmine Giardino

while True:
    percentage = round(float(input("Enter your score (-1 to exit):")))
    if percentage == -1:
        print("Goodbye!")
        break
    if percentage < 0 or percentage > 100:
        print("Please enter a valid score between 0 and 100.")
    elif percentage < 40:
        print("Fail")
    elif percentage < 50:
        print("Pass")
    elif percentage < 60:
        print("Merit 1")
    elif percentage < 70:
        print("Merit 2")
    else:
        print("Distinction")
