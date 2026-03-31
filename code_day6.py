# Day - 6 Tuples
# Tuples are the collection of elements(value)
# This are immutable

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

# 10
# 20

# 1
# 2
# 3

# Sum = 10
