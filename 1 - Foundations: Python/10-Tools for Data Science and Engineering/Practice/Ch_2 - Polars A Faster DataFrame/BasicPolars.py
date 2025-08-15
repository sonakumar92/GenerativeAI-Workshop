# Example file for Advanced Python: Top Tools for Data Science
# Using the Polars library create and access a DataFrame

import polars as pl

data = {
    'Product': ['Laptop', 'Smartphone', 'Tablet', 'Laptop', 'Smartphone', 'Tablet', 'Laptop', 'Smartphone'],
    'Region': ['North', 'North', 'North', 'South', 'South', 'South', 'East', 'East'],
    'SalesAmount': [1200.00, 800.00, 400.75, 1500.25, 900.80, 500.68, 1300.40, 850.72],
    'Quarter': ['Q1', 'Q1', 'Q1', 'Q2', 'Q2', 'Q2', 'Q3', 'Q3'],
    'Year': [2025, 2025, 2025, 2025, 2025, 2025, 2025, 2025]
}

# 1. Create a DataFrame from the data object


# 2. Get information about the DataFrame


# 3. Accessing specific columns


# 4. Adding a new column for Discounted Sales (10% discount)


# 5. Extend a DataFrame with a new row of data
# new_row = pl.DataFrame({
#     'Product': ["Laptop"],
#     'Region': ["West"],
#     'SalesAmount' : [1400.00],
#     'Quarter' : ["Q4"],
#     'Year': [2025]
# })


# 6. Select a set of rows using the slice() method
