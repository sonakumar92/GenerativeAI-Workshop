# Example file for Advanced Python: Top Tools for Data Science
# Using the Pandas library create and access a DataFrame


import pandas as pd

# Create a dataset for sales data
data = {
    'Product': ['Laptop', 'Smartphone', 'Tablet', 'Laptop', 'Smartphone', 'Tablet', 'Laptop', 'Smartphone'],
    'Region': ['North', 'North', 'North', 'South', 'South', 'South', 'East', 'East'],
    'SalesAmount': [1200, 800, 400, 1500, 900, 500, 1300, 850],
    'Quarter': ['Q1', 'Q1', 'Q1', 'Q2', 'Q2', 'Q2', 'Q3', 'Q3'],
    'Year': [2025, 2025, 2025, 2025, 2025, 2025, 2025, 2025]
}

# 1. Create a DataFrame from the data object


# 2. Display the DataFrame


# 3. Using describe() and info()


# 4. Accessing specific columns


# 5. Adding a new column for Discounted Sales (10% discount)


# 6. Add a new row using the concat() function
# new_row = pd.DataFrame({
#     'Product': ["Laptop"],
#     'Region': ["West"],
#     'SalesAmount' : [1400],
#     'Quarter' : ["Q4"],
#     'Year': [2025]
# })


# 7. Use the loc[] and iloc[] accessors to select row ranges
