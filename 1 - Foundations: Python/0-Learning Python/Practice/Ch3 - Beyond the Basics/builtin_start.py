# Example file for using built-in functions
#

mystring = "The quick, brown fox jumped over the lazy dog!"
mylst = [1,3,5,6,9,12,14,17,20,30]

# the len() function calculates the length of a sequence
print(len(mystring)) # Output: 43
print(len(mylst))    # Output: 10

# the max() and min() functions will find the largest and smallest value in a sequence
print(max(mylst))    # Output: 30
print(min(mylst))    # Output: 1

# the str() function will return a string version of an object
prefix = "result: "
result = 5

print(prefix + str(result)) # Output: result: 5
print(str(3.1415)) # Output: 3.1415

# range(start, stop, step) will create a range of numbers
# You can use ranges along with loops
for i in range(5, len(mystring), 2):
    print(mystring[i]) # Output: i, r, ,r o jme vr h a o!

for j in range(2, 20, 4):
    print(j) # Output: 2, 6, 10, 14, 18

# the print function itself is pretty flexible - you can embed variables directly in it
greeting = "Hello!"
count = 10

print(f"{greeting} You have {count} new messages.") # Output: Hello! You have 10 new messages.
