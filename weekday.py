# Write a program that outputs whether or not today is a weekday.
# Author: Carmine Giardino
# Ref to retrieve the current day of the week: https://www.w3schools.com/python/python_datetime.asp

import datetime

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
today = datetime.datetime.now()

if (today.strftime("%A") in weekdays):
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")

'''
# Alternative way
if (today.weekday() < 5):
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")
'''
