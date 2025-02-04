# sum of two amounts in cents and print the result in euros
# author: Carmine Giardino

try:
    amount1 = int(input("Enter amount1(in cent):"))
    amount2 = int(input("Enter amount2(in cent):"))
    total_cents = amount1 + amount2
    total_euros = total_cents / 100
    print("The sum of these is €", total_euros)
except ValueError:
    print("Error: Please enter a valid integer amount.")