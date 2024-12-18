#!/usr/bin/env python3

"""
This script takes numbers from stdin (\n-separated) and displays
a histogram showing the distribution of the input numbers.
"""

import sys
from matplotlib import pyplot as plt
import seaborn as sns

# Check for command-line arguments
if len(sys.argv) > 1:
    try:
        bins = int(sys.argv[1])
    except ValueError:
        print("Invalid number of bins. Please provide an integer.")
        sys.exit(1)
else:
    bins = 10  # Default number of bins

if len(sys.argv) > 2:
    output_file = sys.argv[2]
else:
    output_file = 'histogram.pdf'  # Default output file name

# Read numbers from stdin
numbers = [float(line.strip()) for line in sys.stdin if line.strip()]

# Create histogram
plt.hist(numbers, bins=bins, edgecolor='black')
plt.title('Histogram of Input Numbers')
plt.xlabel('Value')
plt.ylabel('Count')

# Save the plot to a PDF
plt.savefig(output_file)