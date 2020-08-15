from plot import plot

import random
# Test array 
arr = [ 2, 3, 4, 10, 40, 60, 80, 100]
x = 100

# The approach: create arrays to show the performance curve.
# task1: create the plot function.
# for each size N, save the number of iterations in an array.
size = [1, 2, 3, 4]
iters = [1, 4, 9, 16]

# and graph it
plot (size, iters)