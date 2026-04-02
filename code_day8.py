# Day - 8 Sats
# A set is a collection of unique elements
# No duplicate valued are allowed
# Set is Mutable 

# Syntax
set_name = {item1,item2,item3}

# Example - 1
numbers = {10,20,30}
print(numbers)

# Example - 2
numbers = {1,2,3}
numbers.add(4)
print(numbers)

# Example - 3
numbers = {1,2,3}
numbers.remove(2)
print(numbers)

# Example - 4
numbers = {1,2,3,4}
for num in numbers:
  print(num)

# Expected Output
# {10,20,30}

# Expected Output
# {1,2,3,4}

# Expected Output
# {1,3}

# Expected Output
# 1
# 2
# 3
# 4

# Example - Mutable
numbers = {1,2,3}
numbers.update([4,5]) # change element
print(numbers)

# Expected Output
# {1,2,3,4,5}
