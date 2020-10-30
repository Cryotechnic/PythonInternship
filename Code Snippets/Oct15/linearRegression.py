# This file is designed to test linear regression
# Programmed by Ron Friedman, 1926133
# Licensed under GPLv3 License

# Importing libraries
import tensorflow as tf
import pandas as pd
import numpy as np 

# Read file
file = pd.read_csv("mensTime.csv")

# Testing numpy polyfit
results = np.polyfit(file.year, file.mens, 1)
m = results[0]
b = results[1]
m_round = round(m, 3)
b_round = round(b, 3)
print("m = " + str(m_round) + " b = " + str(b_round))

