from plot import plot
from linear_search import linear_search

import random
# Task 4: Create and analyze the linear search function
arr = [ 2, 3, 4, 10, 40, 60, 80, 100]
x = 100

# Function call 
size = []
iters = []
for i in range(10):
    result,count = linear_search(arr, x)
    
    iters.append (count)
    size.append (len(arr))
    if result != -1: 
       print("Element is present at index", str(result)) 
    else: 
       print("Element is not present in array") 
    print("The array of size ", len(arr), "took ", count, "iterations")
    arr+=arr
    arr[len(arr) -1 ] = 1000 + i
    x = 1000 + i

plot (size, iters)