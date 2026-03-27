# Day 2 - Python If,Else,Elif Statements

# Example 1 - Greater than 
num = 10
if num > 5:
  print("Number is greater than 5")
else:
  print("Number is less than or equal to 5")

# Example 2 - Even or Odd
num = 7
if num % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")
  
# Example 3 - Positive/Neagtive/Zero
num = int(input("Enter a number:"))
if num > 0:
  print("Number is positive")
elif num == 0:
  print("Number is Zero")
else:
  print("Number is negative")

# Example 4 - Largest of Two Numbers 
a = int(input("Enter First Number:"))
b = int(input("Enter the Second Number:"))

if a > b:
  print("First number is greater")
elif a == b:
  print("Both numbers are equal")
else:
  print("Second number is greater")


# Expected Output
# Number is greater than 5

# Expected Output
# The number is odd

# Expected Output
# Enter a number: -3
# Number is negative
# Enter a number: 5
# Number is positive

# Expected Output
# Enter First Number:10
# Enter the Second Number:20
# Second number is greater

