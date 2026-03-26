# Day 3 - Functions
# Syntax
def function_name(parameters):
  # code
  return value

# Example 1 (Simple Function)
def greet():
  print("Hello!")

greet()

# Example 2 (Function with Parameter)
def greet(name):
  print("Hello",name)

greet("Srushti")

# Example 3 (Function with Return Value)
def add(a,b):
  return a + b

result = add(5,3)
print(result)

# Example 4 (Real Simple Practice)
def even_odd(n):
  if n % 2 == 0:
    return "Even"
  else:
    return "Odd"

print(even_odd(7))

# Expected Output
# Hello!
# Hello Srushti
# 8
# Odd
