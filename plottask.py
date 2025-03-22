# This script creates:
# 1. A histogram of 1000 values from a normal distribution with mean 5 and standard deviation 2
# 2. A plot of the function h(x) = x^3 over the range [0, 10]

# Ref: https://matplotlib.org/stable/gallery/statistics/hist.html
# Ref: https://matplotlib.org/stable/gallery/lines_bars_and_markers/simple_plot.html

# Author: Carmine Giardino

import matplotlib.pyplot as plt
import numpy as np

# Create data
mean = 5
std_dev = 2
normal_data = np.random.normal(loc=mean, scale=std_dev, size=1000)
line_data = np.linspace(0, 10, 100)
cubic_function = line_data ** 3

# Create the plot
plt.figure(figsize=(10, 6))
plt.hist(normal_data, bins=30, alpha=0.6, label=f'Normal Distribution: μ={mean}, σ={std_dev}')
plt.plot(line_data, cubic_function, color='red', label='Function: $h(x) = x^3$')

# Enhance plot
plt.title('Histogram and Function Plot')
plt.xlabel('x (Input Value)')
plt.ylabel('Frequency / h(x) Value')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('plot.png')
plt.show()
