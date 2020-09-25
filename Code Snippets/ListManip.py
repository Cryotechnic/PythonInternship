# This file is reserved exclusively for List manipulation
# Written by Ron Friedman, 1926133

# Defining list
myList = [1,2,3,4,5,6,7,8,9]
print(myList)

# Defining a list with different types
myList2 = [1.0,-4,"Hello!",True,False,"World!",10]
print(myList2)

# Accessing specific values in list based on index
myList3 = [2.331,"Good ",False,"morning ",-99,12,True,"class!",22]
print(myList3[1] + myList3[3] + myList3[7])

# Modifying specific values in list based on index
myList4 = [2.0,3.33,False,"Python",123,True,"is",321,False,"boring."]
print("This is the unmodified list: ", myList4)
myList4[2] = True
myList4[5] = False
myList4[8] = True
myList4[9] = "cool!"
print("This list should be modified: ", myList4)

# Appending a list 
myList5 = [1.0,2.0,3.0,"I love"]
myList5.append("counting!")
print(myList5)

# Adding lists together
myList6 = ["What a beatiful"]
myList7 = ["day it is!"]
print([myList6] + [myList7])

# Using for loop to go through loop (C -> F)
degreeList = [-50,-45,-40,-35,-30,-25,-20,-15,-10,-5,0,5,10,15,20,25,30,35,40,45,50]
print('C    F')
for C in degreeList:
    F = (9.0/5) * C + 32
    print(C, F)