# Day - 4 Lists
# List is a collection of values/items stored in one variable

# Syntax
list_name = [item1,item2,item3]

# Example 1 : Access Elements
numbers = [10,20,30]
print(numbers[0]) # first element
print(numbers[1]) # Second element

# Example 2 : Add elements
numbers = [1,2,3]
numbers.append(4)
print(numbers)

# Example 3 : Loop through List
numbers = [10,20,30]

for num in numbers:
  print(num)
  
# Example 4 : Find Sum of list
numbers = [1,2,3,4]
total = 0
for num in numbers:
  total += num

print("Sum=",total)

# Expected Output
# 10
# 20

# Expected Output
# [1,2,3,4]

# Expected Output
# 10
# 20
# 30

# Expected Output
# Sum = 10
