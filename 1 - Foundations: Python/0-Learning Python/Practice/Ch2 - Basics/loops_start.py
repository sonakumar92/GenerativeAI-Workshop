# Example file for working with loops


x = 0

print("=================================")
# define a while loop
while (x < 5):
    print(x)
    x += 1

# Output: 0 1 2 3 4
print("=================================")

# define a for loop
for i in range(1, 10):
    print(i)

# Output: 1 2 3 4 5 6 7 8 9
print("=================================")

# use a for loop over a collection
lst = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
for d in lst:
    print(d)

# Output: Mon Tue Wed Thu Fri Sat Sun
print("=================================")

# use the break and continue statements
for i in range(1, 10):
    if (i == 5):
        break
    print(i)

# Output: 1 2 3 4
print("..................")

for i in range(1, 10):
    if (i % 2) == 0:
        continue
    print(i)

# Output: 1 3 5 7 9
print("=================================")

# using the enumerate() function to get an index and an item
for i, d in enumerate(lst):
    print(i, d)

# Output: 0 Mon
#         1 Tue
#         2 Wed
#         3 Thu
#         4 Fri
#         5 Sat
#         6 Sun
