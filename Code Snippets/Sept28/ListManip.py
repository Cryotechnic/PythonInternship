# This file's purpose is to get yourself familiar with 2D lists,
# also known as 2D matrices. 
# Written by Ron Friedman, 1926133

# Importing numpy, which contains several useful mathematical operations
import numpy

# Defining the two lists
list1 = numpy.array([[1, 2], [4, 5]])
list2 = numpy.array([[7, 8], [9, 10]])
list3 = ['cat', 'dog', 'mouse']

# Printing the initial matrices
print(list1, list2)

# Executing addition of matrices
print("Adding both matrices: \n")
(numpy.add(list1, list2)) # FIXME: Not working for some reason (does not display)

# Executing subtraction of matrices 
print("Subtracting both matrices: \n")
(numpy.subtract(list1, list2))

# Executing matrix math
print (numpy.divide(list1,list2))
print ("Multiplication of two matri ces: ") # a * inverse b
print (numpy.multiply(list1,list2))
print ("The product of two matrices: ")
print (numpy.dot(list1,list2))
print ("square root is: ")
print (numpy.sqrt(list1))
print ("The summation of elements: ")
print (numpy.sum(list2))

# Using "T" to transpose the matrix
print ("Matrix transposition: ")
print (list1.T)
print(list2.T)

# List appending 
print("Initial list: ", list3)
list3.append('parrot')
print("Modifified list: ", list3)

# List item insertion
print("Appended list: ", list3)
list3.insert(2, "not an animal here")
print("Inserted list: ", list3)

# Deleting items from list
print("Modified list: ", list3)
list3.remove("not an animal here")
print("Removed list: ", list3)
print("The length of list3 is: ", len(list3))