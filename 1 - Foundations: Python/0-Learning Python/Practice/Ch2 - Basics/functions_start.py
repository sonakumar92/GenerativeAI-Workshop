# Example file for working with functions


# define a basic function
def greet():
    print("Hello, Sona")
greet()
# Output: Hello, Sona
print("-----------------------------")
# function that takes parameters
def greet_with_parm(name):
    print("Hello,", name)
greet_with_parm("Sona")
# Output: Hello, Sona
print("-----------------------------")
# function that returns a value
def return_greeting(name):
    return "Hello, " + name
print(return_greeting("Sona"))
# Output: Hello, Sona
print("-----------------------------")
# function with default value for an parameter
def default_value_greet(greeting, name="Guest"):
    print(greeting, name)

default_value_greet("Nice to meet you", "Mike")
# Output: Nice to meet you Mike
default_value_greet("Nice to meet you")
# Output: Nice to meet you Guest
default_value_greet(name="Joe", greeting="Hi there,")
# Output: Hi there, Joe
default_value_greet(greeting="Hi there,", name="Joe1")
# Output: Hi there, Joe1
print("-----------------------------")
# function with variable number of parameters
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result
print(multi_add(10,4,5,10,4))
# Output: 43
