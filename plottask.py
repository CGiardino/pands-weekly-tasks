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

# Plot the histogram of the normal distribution samples
plt.hist(
    normal_data,
    bins=30,            # Number of histogram bins
    alpha=0.6,          # Transparency of bars
    label=f'Normal Distribution: μ={mean}, σ={std_dev}'  # Legend label
)

# Overlay the cubic function plot on top of the histogram
plt.plot(
    line_data,
    cubic_function,
    color='red',
    label='Function: $h(x) = x^3$'  # LaTeX-style label for the legend
)

# Enhance plot
plt.title('Histogram and Function Plot')
plt.xlabel('x (Input Value)')
plt.ylabel('Frequency / h(x) Value')
plt.legend()
plt.grid(True)
# Avoid overlapping elements
plt.tight_layout()
# Save the figure to a PNG file
plt.savefig('plot.png')
plt.show()
