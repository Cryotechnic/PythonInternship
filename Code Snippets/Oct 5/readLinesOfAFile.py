import tensorflow as tf
import pandas as pd
import numpy as np 
f = open('titanic.csv','r')
listOfLines = f.readlines()
numberOfSurvivors = 0
numberOfMr = 0
numberOfMrs = 0
numberOfMiss = 0
numberOfMaster = 0
numberOfRev = 0
numberOfMlle = 0
numberOfCol = 0
numberOfDr = 0
numberOfLady = 0
numberOfMajor = 0
otherRoles = 0
mistakes = 0
for line in listOfLines:
  if line[0]=='1': numberOfSurvivors+=1
  if "Mr." in line: numberOfMr+=1
  elif "Mrs." in line: numberOfMrs+=1
  elif "Miss." in line: numberOfMiss+=1
  elif "Master." in line: numberOfMaster+=1
  elif "Rev." in line: numberOfRev+=1
  elif "Mlle." in line: numberOfMlle+=1
  elif "Col." in line: numberOfCol+=1
  elif "Dr." in line: numberOfDr+=1
  elif "Lady." in line: numberOfLady+=1
  elif "Major." in line: numberOfMajor+=1
  elif "Don." or "Mme." or "Ms." or "Sir." or "Capt." or "the Countess." or "Jonkheer" in line: otherRoles+=1
  else: mistakes+=1
print("Survivors:" + str(numberOfSurvivors))
print("Mr: " + str(numberOfMr))
print("Mrs: " + str(numberOfMrs))
print("Miss: " + str(numberOfMiss))
print("Master: " + str(numberOfMaster))
print("Rev: " + str(numberOfRev))
print("Mlle: " + str(numberOfMlle))
print("Col :" + str(numberOfCol))
print("Dr: " + str(numberOfDr))
print("Lady: " + str(numberOfLady))
print("Major: " + str(numberOfMajor))
print("Other roles: " + str(otherRoles))
print("Mistakes: " + str(mistakes))
print(len(listOfLines))
f.close()

#another way...

titanic = pd.read_csv("titanic.csv")
print(type(titanic))  #DataFrame or dictionary 
print(titanic.Name) # a column of all the names...
####
print("Survivors based on bins from pandas")
mybins = [0, 100, 200, 400, 513]
mylabels = ['1st qut.', '2nd qut.', '3rd qut.', '4th qut.']
titanic['binned'] = pd.cut(titanic['Fare'], bins = mybins, labels = mylabels)
####
print ("now all the axes of Titanic" )
print (titanic.groupby([ "binned","Survived"] ).size() )
print (titanic.axes)
print("now all the columns")
print(titanic.columns)
#### Sorting by male and female
print("Sorting by male and female")
print(titanic.groupby(["Sex", "Survived"]).size())
####
numberOfSurvivors = 0
numberOfMr = 0
numberOfMrs = 0
numberOfMiss = 0
numberOfMaster = 0
numberOfRev = 0
mistakes = 0
series = pd.Series(titanic.Survived)
print ("now printing the value counts of Survived")
print ( titanic.Survived.value_counts())
print ("now printing a series of survived value")
print(series)
print("Survivors: \n" + str( series.value_counts()[1] ))
seriesOfNames = pd.Series(titanic.Name)
print( "Now series contain names" )
for string in seriesOfNames:
  if ( "Mr." in string ):numberOfMr+=1

print("Mr " + str(numberOfMr))
print("Mrs " + str(numberOfMrs))
print("Miss " + str(numberOfMiss))
print("Master " + str(numberOfMaster))
print("Rev " + str(numberOfRev))
print("oupppsss" + str(mistakes))
print(len(listOfLines))
f.close()



