# Example file for Advanced Python: Top Tools for Data Science
# Using the Polars library Lazy API to defer execution

import polars as pl

data = {
    'Product': ['Laptop', 'Smartphone', 'Tablet', 'Laptop', 'Smartphone', 'Tablet', 'Laptop', 'Smartphone'],
    'Region': ['North', 'North', 'North', 'South', 'South', 'South', 'East', 'East'],
    'SalesAmount': [1200.00, 800.00, 400.75, 1500.25, 900.80, 500.68, 1300.40, 850.72],
    'Quarter': ['Q1', 'Q1', 'Q1', 'Q2', 'Q2', 'Q2', 'Q3', 'Q3'],
    'Year': [2025, 2025, 2025, 2025, 2025, 2025, 2025, 2025]
}

# 1. Create a DataFrame from the data object


# 2. Create a query and use the explain() function to see what's going to happen
