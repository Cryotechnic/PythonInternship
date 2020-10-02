# This file explores different control statements, 
# such as while, if and for
# Programmed by Ron Friedman, 1926133

# Importing libraries 

# Using While loops
list1 = ['cat', 'dog', 'mouse']
print("Original list: ", list1)

while list1:
    print("Modified list: ", list1.pop(-1)) # This will remove 1 element until there are no more elements left

# Combining if and for loops
x = [80, 70, 65, 60, 50, 40, 45, 40, 35, 7, 0, -1, -122, -23, -5] # Random number distribution
for y in x:
    if y >= 50:
        print("Good")
    elif y <= 50 and y >= 0:
        print("Value lower than 50")
    else:
        print("Bad")

# Using range with lists
list2 = []
startVal, endVal = 1, 100
if startVal < endVal:
    list2.extend(range(startVal, endVal))
    list2.append(endVal)
print(list2)