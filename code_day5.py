# Day -5 Strings
# A String is a sequence of characters (text) enclosed with single or double quotes.
# Strings are Immutable(cannot change)

# Syntax
string_name = "Text"

# Example - 1
# String using single quote 
name1 = 'Srushti'

# String using double quote 
name2 = "Srushti"

# Print both values
print(name1)
print(name2)

# Example - 2
# Store a string
text = "Python"

# Print the string
print(text)

# Example - 3
# String
text = "Python"

# Access characters using index(starts from 0)
print(text[0]) # First character
print(text[1]) # Second character

# Example - 4
# String
text = "Python"

# Find length of string
print(len(text))

# Example - 5
# String
text = "python"

# Convert to uppercase 
print(text.upper())

# Convert to lowercase
print(text.lower())

# Example - 6
# String
text = "Hi"

# Loop through each character
for ch in text:
  print(ch) # Print each character inside text

# Example - 7
# String
text = "hello"

# Initialize counter
count = 0

# Loop through each character
for ch in text:
  # Check if character is a vowel
  if ch in "aeiou":
    count += 1 # Increase count
    
# Print results
print("Vowels=",count)

# Expected Output:

# Srushti
# Srushti

# Python

# P
# h

# 6

# PYTHON
# python

# H
# i

# Vowels = 2

# Example - Immutable
text = "hello"
text[0] = "H" # not allowed

# Output : Error
