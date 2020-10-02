# This file is designed to read a file and output it to the user
# Programmed by Ron Friedman, 1926133

# Importing libraries
import csv

# Opening file and printing to user
# Using 'with' as it lets me reference the CSV as a variable

with open('titanic.csv', 'r') as file:
    output = csv.reader(file)
    for row in output:
        print(row)

