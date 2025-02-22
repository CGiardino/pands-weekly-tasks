# add two cents amounts
# author: Carmine Giardino
# takes two user input amounts in cents, sums them,
# and prints the result in euros.

try:
    amount1 = int(input("Enter amount1(in cent):"))
    amount2 = int(input("Enter amount2(in cent):"))
    total_cents = amount1 + amount2
    total_euros = total_cents / 100
    print("The sum of these is €", total_euros)
except ValueError:
    print("Error: Please enter a valid integer amount.")