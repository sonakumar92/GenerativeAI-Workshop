# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
lst = [1, 'Hi', 2.34, True, 9]
print(len(lst)) # Output: 5
print(lst) # Output: [1, 'Hi', 2.34, True, 9]

# Lists are mutable, meaning you can change their content
lst[0] = 100
print(lst) # Output: [100, 'Hi', 2.34, True, 9]

# Add new items to the list
lst.append('New Item')
print(lst) # Output: [100, 'Hi', 2.34, True, 9, 'New Item']

# Delete items from the list
del lst[3]
print(lst) # Output: [100, 'Hi', 2.34, 9, 'New Item']

# to access a member of a sequence type, use []
print(lst[0]) # Output: 100'
print(lst[1]) # Output: 'Hi'
print(lst[-1]) # Output: 'New Item'

# add a list to another list
lst2 = [10, 20, 30, 40, 50]
lst3 = [60, "Hello"]

lst_join = lst2 + lst3
print(lst_join) # Output: [10, 20, 30, 40, 50, 60, 'Hello']

#lst_plus = lst2 + 10 # TypeError: can only concatenate list (not "int") to list
#lst_minus = lst2 - 10 # TypeError: unsupported operand type(s) for -: 'list' and 'int'

# This line multiplies the list lst2 by 3 and assigns the result to lst_multi.
# How it works
# In Python, multiplying a list by an integer repeats the list that many times.
# For example, if lst2 = [1, 2], then lst2 * 3 results in [1, 2, 1, 2, 1, 2].
lst_multi_times = lst2 * 3
print(lst_multi_times) # Output: [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]

#lst_multi = lst2 / 3 # TypeError: unsupported operand type(s) for /: 'list' and 'int'

print(lst2) # Output: [10, 20, 30, 40, 50]
print(lst3) # Output: [60, 70]

# use slices to get parts of a sequence
print(lst2[2:4]) # Output: [30, 40]
print(lst2[:2]) # Output: [10, 20]
print(lst2[1:]) # Output: [20, 30, 40, 50]

# you can use slices to reverse a sequence
print(lst2[::-1]) # Output: [50, 40, 30, 20, 10]
print(lst2[1::]) # Output: [20, 30, 40, 50]
print(lst2[3::]) # Output: [40, 50]
print(lst2[3::-1]) # Output: [40, 30, 20, 10]

# Tuples are like lists, but they are immutable
mytuple = (1, 2, 3, 'Hi')
print(mytuple) # Output: (1, 2, 3, 'Hi')

print(mytuple[0]) # Output: 1
print(mytuple[-1]) # Output: 'Hi'
print(mytuple[1:3]) # Output: (2, 3)

# del mytuple[0] # This will cause an error because tuples are immutable

# Tuples can be nested
mynestedtuple = (1, 2, (3, 4), 5)
print(mynestedtuple) # Output: (1, 2, (3, 4), 5)

# Sets are also sequences, but they contain unique values
myset = {7, 1, 2, 6, 3, 4, 5, 3}
print(myset) # Output: {1, 2, 3, 4, 5, 6, 7}

# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error

# Test for membership
print(1 in myset) # Output: True
print(9 in myset) # Output: False
