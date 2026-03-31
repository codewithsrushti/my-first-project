# Day - 6 Tuples
# Tuples are the collection of elements(value)
# This are Immutable

# Syntax
tuple_name = (item1,item2,item3)

# Example - 1
numbers = (10,20,30)
print(numbers)

# Example - 2
numbers = (10,20,30)
print(numbers[0])
print(numbers[2])

# Example - 3
numbers = (1,2,3)
for num in numbers:
  print(num)

# Example - 4
numbers = (1,2,3,4)
total = 0

for num in numbers:
  total += num

print("Sum = ",total)

# Excpected Output
# (10,20,30)

# Expected Output
# 10
# 20

# Expected Output
# 1
# 2
# 3

# Expected Output
# Sum = 10

# Example - Immutable
numbers = (10,20,30)
numbers[0] = 15 # not allowed

# Output : TypeError :'tuple' object doesnot support item assignment
