# -*- coding: utf-8 -*-

# if (condition):
    # Do something

x = "t"
if x == "A":
  print("Yes, it is A!")


x = "A"
if x == "A":
  print("Yes, it is A!")
else:		
  print("No, it is not A!")


x = "B"
if x == "A":
  print("It is A!")
elif x == "B":
  print("It is B!")
elif x == "C":
  print("It is C!")  
elif x == "D":
  print("It is A!")  
else:
  print("No, it is not A!")


x = "T"
if x == "A" or x == "G":
  print("It is Purine!")
elif x == "C" or x == 'T' or x == "U":
  print("It is Pyrimidine!")
else:	
  print("It is neither Purine nor pyrimidine!")
