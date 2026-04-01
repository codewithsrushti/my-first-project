# Day -7 Dictonary 
# A Dictonary stores data in key:value pairs
# A Dictonary is mutable collection of key-value pairs

# Syntax
dict_name = { key1:value1,key2:value2}

# Example -1 
student = {"name":"Srushti","age":20}

print(student)

# Example -2 
student = {"name":"Srushti","age":20}

print(student["name"])

# Example - 3
student = {"name":"Srushti","age":20}

student["age"] = 21 # update
student["Course"] = "CSE" # add

print(student)

# Example - 4
student = {"name":"Srushti","age":20}

for key in student:
  print(key,":",student[key])

# Expected Output
# {'name':Srushti','age':20}

# Expected Output
# Srushti

# Expected Output
# {'name':'Srushti','age':21,'Course':'CSE'}

# Expected Output
# name : Srushti
# age : 20
