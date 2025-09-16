# Working with modules of code

# import the math module, which contains features for working with mathematics
import math

print(math.sqrt(16)) # Output: 4.0

# import a specific part of the module so you can refer to it more easily
from math import pi
print(pi) # Output: 3.141592653589793

# import a module and give it a different name
import random as r
print(r.randint(100, 200)) # Output: Random number between 100 and 200

# the math module contains lots of pre-built functions
print(math.factorial(5)) # Output: 120
print(math.log(100, 10)) # Output: 2.0
print(math.pi) # Output: 3.141592653589793

# Generate a random number between 100 and 200
print(r.randint(100, 200)) # Output: Random number between 100 and 200

# Use the 3rd party tabulate module to print tabulated data:
# install tabulate
# python3 -m pip install tabulate
from tabulate import tabulate

# Sample data
data = [
  ["Product", "Price", "Stock"],
  ["Laptop", 999.99, 45],
  ["Mouse", 24.99, 128],
  ["Keyboard", 59.99, 89]
]

# Create a formatted table
print(tabulate(data, headers="firstrow", tablefmt="grid"))
# output:
# +-----------+--------+--------+
# | Product   |  Price |  Stock |
# +===========+========+========+
# | Laptop    |  999.99|     45 |
# +-----------+--------+--------+
# | Mouse     |   24.99|    128 |
# +-----------+--------+--------+
# | Keyboard  |   59.99|     89 |
# +-----------+--------+--------+

# Create a formatted table (use tabulate if available, otherwise simple fallback)
if tabulate:
    print(tabulate(data, headers="firstrow", tablefmt="grid"))
else:
    headers = data[0]
    rows = data[1:]
    col_widths = [max(len(str(cell)) for cell in col) for col in zip(*([headers] + rows))]
    row_fmt = " | ".join(f"{{:{w}}}" for w in col_widths)
    print(row_fmt.format(*headers))
    print("-" * (sum(col_widths) + 3 * (len(col_widths) - 1)))
    for r in rows:
        print(row_fmt.format(*r))

