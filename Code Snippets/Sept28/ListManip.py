# This file's purpose is to get yourself familiar with 2D lists,
# also known as 2D matrices. 
# Written by Ron Friedman, 1926133

# Importing numpy, which contains several useful mathematical operations
import numpy

# Defining the two lists
list1 = numpy.array([[1, 2], [4, 5]])
list2 = numpy.array([[7, 8], [9, 10]])

# Printing the initial matrices
print(list1, list2)

# Executing addition of matrices
print("Adding both matrices: \n")
(numpy.add(list1, list2)) # FIXME: Not working for some reason (does not display)

# Executing subtraction of matrices 
print("Subtracting both matrices: \n")
(numpy.subtract(list1, list2))

# print ("Matrix Division : ")
print (numpy.divide(list1,list2))
print ("Multiplication of two matri ces: ")
print (numpy.multiply(list1,list2))
print ("The product of two matrices: ")
print (numpy.dot(list1,list2))
print ("square root is: ")
print (numpy.sqrt(list1))
print ("The summation of elements: ")
print (numpy.sum(list2))
# using "T" to transpose the matrix
print ("Matrix transposition: ")
print (list1.T)