# Example file for Advanced Python: Top Tools for Data Science
# Using the Faker library to generate numerical data


import faker


# Create Faker instance
fake = faker.Faker()

# Basic number generation
# print(fake.random_number())
# print(fake.random_int())  # Default: 0 to 9999
# print(fake.pydecimal())  # Default decimal
# print(fake.pyfloat())  # Default float
# print(fake.pybool())  # Default boolean

# Generating numbers with constraints
# print(fake.random_number(digits=5, fix_len=True))
# print(fake.random_int(min=100, max=999))  # Custom range
# print(fake.random_int(min=-1000, max=-1))  # Negative numbers
# print(fake.pydecimal(min_value=10000, max_value=99999))  # Range constraint

# Sequences and patterns
# print(fake.random_int(min=2, max=100, step=2))  # Even numbers
# print(fake.random_int(min=1, max=99, step=2))  # Odd numbers
# print(fake.random_int(min=5, max=100, step=5))  # Multiples of 5

# Special number formats
# print(fake.pydecimal(left_digits=4, right_digits=2, positive=False))  # Format: XXX.XX
# print(fake.pyfloat(min_value=0, max_value=1000, right_digits=2))  # Percentage

# Numbers for specific use cases
# print(fake.random_digit())
# print(fake.random_digit_not_null())
# print(fake.latitude())  # Geographic coordinate
# print(fake.longitude())  # Geographic coordinate
