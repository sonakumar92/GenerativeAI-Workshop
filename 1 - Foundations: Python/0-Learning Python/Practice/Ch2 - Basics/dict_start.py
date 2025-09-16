# Example file for complex types


# mydictionary: a key-value data structure
mydict = {
    "one": 1,
    "two": 2,
    3: "three",
    4.5: ["four", "point", "five"],
}  

print(mydict)
# Output: {'one': 1, 'two': 2, 3: 'three', 4.5: ['four', 'point', 'five']}

# mydictionaries are accessed via keys
print(mydict["one"]) # Output: 1
print(mydict[3])     # Output: three
print(mydict[4.5])   # Output: ['four', 'point', 'five']

# you can also set mydictionary data by creating a new key
mydict["five"] = 5
print(mydict)
# Output: {'one': 1, 'two': 2, 3: 'three', 4.5: ['four', 'point', 'five'], 'five': 5}


# Trying to access a nonexistent key will produce an error
# print(mydict["nine"]) # KeyError: 'nine'

# To avoid this, you can use the "in" operator to see if a key exists
if "nine" in mydict:
    print(mydict["nine"])
else:
    print("Key 'nine' not found.")

# You can retrieve all of the keys and values from a mydictionary
print(mydict.keys())   # Output: dict_keys(['one', 'two', 3, 4.5, 'five'])
print(mydict.values()) # Output: dict_values([1, 2, 'three', ['four', 'point', 'five'], 5])
print(mydict.items())  # Output: dict_items([('one', 1), ('two', 2), (3, 'three'), (4.5, ['four', 'point', 'five']), ('five', 5)])

# You can also iterate over all the items in a mydictionary
for key, value in mydict.items():
    print(f"Key: {key}, Value: {value}")

# Output:
# Key: one, Value: 1
# Key: two, Value: 2
# Key: 3, Value: three
# Key: 4.5, Value: ['four', 'point', 'five']
# Key: five, Value: 5   