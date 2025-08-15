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

# Create a DataFrame from the data object
# df = pl.DataFrame(data)
# print(df)


# Get information about the DataFrame
# print("\nBasic DataFrame structure:")
# print(df.schema)
# print(df.shape)
# print(df.columns)
# print(df.describe())


# Accessing specific columns
# print(df.select("Product","SalesAmount"))


# Adding a new column for Discounted Sales (10% discount)
# df = df.with_columns(SalesEuros = pl.col("SalesAmount") * 0.9)
# print(df)


# Extend a DataFrame with a new row of data
# new_row = pl.DataFrame({
#     'Product': ["Laptop"],
#     'Region': ["West"],
#     'SalesAmount' : [1400.00],
#     'Quarter' : ["Q4"],
#     'Year': [2025]
# })
# df.extend(new_row)
# print(df)


# Select a set of rows using the slice() method
# subset_df = df.slice(1, 3)
# print(subset_df)
