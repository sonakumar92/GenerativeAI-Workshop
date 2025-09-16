# Example file for working with Exceptions
#

# Errors can happen in programs, and we need a clean way to handle them
# This code will cause an error because you can't divide by zero:
try:
    x = 10 / 0
    print(x)
except:
    print("Well that didn't work!")
# Output: Well that didn't work!

# Exceptions provide a way of catching errors and then handling them in 
# a separate section of the code to group them together
try:
    x = 10 / 0
    print(x)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
# Output: Error: Division by zero is not allowed.

# You can also catch specific exceptions
try:
    x = int("er3")
except ValueError:
    print("Error: Invalid input. Please enter a number.")
# Output: Error: Invalid input. Please enter a number.

# With finally
try:
    x = 10 / 0
    print(x)
except ZeroDivisionError:
    print("Well that didn't work!")
finally:
    print("This will always execute.")
# Output: Well that didn't work!
#         This will always execute.
