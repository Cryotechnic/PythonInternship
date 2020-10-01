# This file is reserved for functions that are going to be used in MainFile.py
# Written by Ron Friedman, 1926133
# Functions currently implemented:

# Math function

def mathFunc():
    print("Welcome to the math function! It will calculate the minimum and maximum of a list.")
    myList = [1,2231,1231,2566,12,6775]
    print("The minimum of the list is ", min(myList), "and the maximum of the list", max(myList))
    print("Successfully calculated!")

# List function
def listFunc():
    myList2 = ["What a beatiful"]
    myList3 = ["day it is!"]
    print([myList2] + [myList3])

def stringFunc():
    print("Testing string function now!")
    word1 = "It "
    word2 = "works!"
    print(word1 + word2)
    print("Success!")