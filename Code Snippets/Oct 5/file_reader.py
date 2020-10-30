# This file is designed to smoothly access and read files, line by line
# using the pandas package. Each line is separated by the /n character sequence
# while outputing in DataFrames, then converting to dictionaries
# Programmed by Ron Friedman, 1926133



# Importing libraries
import pandas as pd

# Reading file and printing first 100 rows
file = pd.read_csv("titanic.csv")
#print(file.head(100))

# Converting to dictionary
dict1 = file.to_dict()
print(dict1)

# Selecting between range
