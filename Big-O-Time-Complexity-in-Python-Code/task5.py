from plot import plot
from binary_search import binary_search
import random

# task 5: Create and analyze the binary_search function
arr = [0, 10, 20, 30, 40, 50, 60]
x = 6
result, count = binary_search(arr, 0, len(arr)-1, x)
#initial test
# Test array 
arr = [ 2, 3, 4, 10, 40, 60, 80, 100]
x = 100
# Function call 
size = []
iters = []
for i in range(10):
    
    #task 4 -- using tuple
    result, count = binary_search(arr, 0, len(arr)-1, x)
    
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