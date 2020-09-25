# This file is reserved for string manipulation and testing

# Importing libraries

# Creating initial words
word = "Hello, "
word2 = "World!"
wordNull = ""

# Printing words

print(word)
print(wordNull)

# Using index to retrieve specific letter
letter = word[0]
print(letter)

# String concatenation (adding)
word3 = word + word2
print(word3)

# Modifying string (inserting new characters)
word4 = "Goodbye World! " + word + word2
print(word4)

# Removing from string (deleting characters) FIXME: Does not work!
word5 = "Goodbye World!"
word6 = ""
if word5.find("Goodbye"):
   word5.replace(" ") 
print(word5)

