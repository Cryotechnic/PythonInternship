# This file will contain the main function that will call upon other functions in other files
# Written by Ron Friedman, 1926133

from HelloWorld import testFunc  
from FuncFile import mathFunc, listFunc, stringFunc
import time
def main():
    print("This function will now go through each function and test them.")
    time.sleep(3) # Delays next line by 3 seconds
    print("Executing test function...")
    testFunc()
    time.sleep(3)
    print("Executing math function...")
    mathFunc()
    time.sleep(3)
    print("Executing list function...")
    listFunc()
    time.sleep(3)
    print("Executing String function...")
    stringFunc()
    time.sleep(2)
    print("If you've gotten this far without any errors")
main()