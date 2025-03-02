# Write a program that outputs whether or not today is a weekday.
# Author: Carmine Giardino
# Ref to retrieve the current day of the week: https://www.w3schools.com/python/python_datetime.asp

import datetime

today = datetime.datetime.now()
if (today.weekday() < 5):
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")
