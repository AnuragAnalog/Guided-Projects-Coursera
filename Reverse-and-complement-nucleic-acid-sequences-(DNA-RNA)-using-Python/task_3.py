# -*- coding: utf-8 -*-

# use print() function to print different data types
print('test')
print(1)
x = 24.7
print(x)

# print series of numbers from 1 to 5
print(1)
print(2)
print(3)
print(4)
print(5)

# Use variable as a counter
x = 1
print(x)
x = x +1
print(x)
x = x +1
print(x)
x = x +1
print(x)
x = x +1
print(x)


for i in range(5):
    print(i)


for i in range(1, 6):
    print(i)


for i in range(1,6):
    for j in range(1,4):
        print(i)
        print(j)


for i in range(1,6):
    for j in range(1,4):
        print('i =', i, '&', 'J =', j )


for i in range(1, 10):
    print([*range(i)])
for i in range(10, 1, -1):
    print([*range(i)])
