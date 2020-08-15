
from return_element import return_element

import random
from plot import plot
arr = [10, 8, 6, 4, 2, 1]
x = 100
size = []
iters = []
for i in range(10):
    # task 2: create the return_element function
    # gen a random index into the array
    index = random.randint(0,len(arr)-1)
    result, count = return_element(arr, index)
    iters.append (count)
    size.append (len(arr))
    
    arr+=arr
    
plot (size, iters)