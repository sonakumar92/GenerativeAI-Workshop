# Example file for Advanced Python: Top Tools for Data Science
# Using the Polars library to read and write data files

import polars as pl


# Read a CSV file
df = pl.read_csv("sales_data.csv")
print(df)

# Use only a subset of the columns
df = pl.read_csv("sales_data.csv", n_rows=5, columns=["Product", "Region", "SalesAmount"], new_columns=["Prod","Reg","Sales"])
print(df)


# read a JSON file
df = pl.read_json("sample-weather-data.json")
print(df.head())


# Read an Excel file and convert it to a CSV file
df = pl.read_excel("FinancialSample.xlsx", nrows=20)
df.to_csv("Financials.csv")
