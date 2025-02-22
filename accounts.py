# Weekly Task 03
# Author: Carmine Giardino
# This program reads in a 10 caracter account number
# and outputs the account number with only the last 4 digits shown.

# Resources:
# https://www.datacamp.com/tutorial/f-string-formatting-in-python
# https://www.w3schools.com/python/python_strings_slicing.asp

account_number = input("Please enter an 10 digit account number: ")
offuscated_numbers = "X" * 6
if len(account_number) != 10:
    print("Error: Please enter a valid 10 digit account number.")
else:
    print(f"{offuscated_numbers}{account_number[6:]}")

# Extra:
# Modify the program to deal with account numbers of any length
# By using len() function we can get the length of the slice without the last
# 4 digits and replace them with "X"

account_number_any_length = input(
    "Please enter an account number of any length: "
)
offuscated_numbers = "X" * len(account_number_any_length[:-4])
print(f"{offuscated_numbers}{account_number_any_length[-4:]}")
