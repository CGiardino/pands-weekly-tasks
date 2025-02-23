# generates 10 random numbers (0-100) and prints them out and prints the top 3
# Author: Carmine Giardino

import random
random_numbers = []
top_three = []
for i in range(10):
    random_numbers.append(random.randint(0, 100))
print("10 random numbers: ", random_numbers)
random_numbers.sort(reverse=True)
top_three = random_numbers[:3]
print("Top 3: ", top_three)
