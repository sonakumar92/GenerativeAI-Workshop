# Example file for variables and basic types


# Basic data types in Python: Numbers, Strings, Booleans 
# Variable names must start with a letter or _, and can have numbers. They are case sensitive. 
myint = 10
myfloat = 12.25
mystr = "Hello string"
mybool = True
# We can display the content of a variable using the print() function
print("-------------------------------------")
print("display the content of a variable \nusing the print() function:")
print("-------------------------------------")
print("STEP 1...............................")
print(myint) # Output: 10
print(myfloat) # Output: 12.25
print(mystr) # Output: Hello string
print(mybool) # Output: True
print("STEP 2...............................")
print("INT: " + str(myint)) # Output: INT: 10
print("FLOAT:  " + str(myfloat)) # Output: FLOAT: 12.25
print("STRING:  " + mystr) # Output: STRING:  Hello string
print("BOOLEAN:  " + str(mybool)) # Output: BOOLEAN:  True
print("STEP 3...............................")
print(f"INT:  {myint}") # Output: INT:  10
print(f"FLOAT:  {myfloat}") # Output: FLOAT:  12.25
print(f"STRING:  {mystr}") # Output: STRING:  Hello string
print(f"BOOLEAN:  {mybool}") # Output: BOOLEAN:  True
print("STEP 4...............................")
print("INT:  {myint}") # This will print INT:  {myint}
print("FLOAT:  {myfloat}") # This will print FLOAT:  {myfloat}
print("STRING:  {mystr}") # This will print STRING:  {mystr}
print("BOOLEAN:  {mybool}") # This will print BOOLEAN:  {mybool}
print("STEP 4...............................")
#print("INT: " + myint) # this will cause an error TypeError: can only concatenate str (not "int") to str
#print("FLOAT:  " + myfloat) # this will cause an error TypeError: can only concatenate str (not "float") to str
print("STRING:  " + mystr) # Output: STRING:  Hello string
#print("BOOLEAN:  " + mybool) # this will cause an error TypeError: can only concatenate str (not "bool") to str
# Operators are used to perform operations on variables
print("-------------------------------------")
# Arithmetic operators
a = 15
b = 4
print("Arithmetic operators:")
print("-------------------------------------")
print(f"{a} + {b} = {a + b}") # Output: 15 + 4 = 19
print(f"{a} - {b} = {a - b}") # Output: 15 - 4 = 11
print(f"{a} * {b} = {a * b}") # Output: 15 * 4 = 60
# float division
print(f"{a} / {b} = {a / b}") # Output: 15 / 4 = 3.75
# integer (floor) division
print(f"{a} // {b} = {a // b}")
# remainder
print(f"{a} % {b} = {a % b}")  # Output: 15 % 4 = 3
# exponentiation
print(f"{a} ** {b} = {a ** b}") # Output: 15 ** 4 = 50625
print("-------------------------------------")
# Assignment operators
c = 10
print("Assignment operators:")
print("-------------------------------------")
print("c =", c) # Output: c = 10
c += 5
print("c += 5 ->", c) # Output: c += 5 -> 15
c *= 2
print("c *= 2 ->", c) # Output: c *= 2 -> 30    
print("-------------------------------------")
# Comparison operators (produce booleans)
x = 7
y = 10
print("Comparison operators:")
print("-------------------------------------")
print(f"{x} == {y} ->", x == y) # Output: False
print(f"{x} != {y} ->", x != y) # Output: True
print(f"{x} < {y}  ->", x < y)  # Output: True
print(f"{x} <= {y} ->", x <= y) # Output: True
print(f"{x} > {y}  ->", x > y)  # Output: False
print(f"{x} >= {y} ->", x >= y) # Output: False
print("-------------------------------------")
# Logical operators
p = True
q = False
print("Logical operators:")
print("-------------------------------------")
print("p and q ->", p and q) # Output: False
print("p or q  ->", p or q) # Output: True
print("not p   ->", not p)  # Output: False
print("-------------------------------------")
# Membership and identity examples
str = "hello"
lst = [1, 2, 3]
print("Membership and identity:")
print("-------------------------------------")
print("'h' in str ->", 'h' in str) # Output: True
print("2 in lst ->", 2 in lst) # Output: True
print("lst is lst ->", lst is lst) # Output: True
print("lst is str ->", lst is str) # Output: False
print("-------------------------------------")
# re-declaring a variable works
print("re-declaring a variable works")
print("-------------------------------------")
myint = "abc"
print(myint) # Output: abc
print("-------------------------------------")
