# Example file for Advanced Python: Top Tools for Data Science
# Using the Pandas library create and access a DataFrame


import pandas as pd


# Read data from a CSV file and describe the DataFrame
df = pd.read_csv("sales_data.csv")
print(df)


# Use only a subset of the columns
df = pd.read_csv("sales_data.csv", usecols=["Product", "Region", "SalesAmount"])
print(df)


# Read a JSON file, limiting the number of rows
df = pd.read_json("sample-weather-history.json")
df = df.set_index("date")
print(df.head(20))


# Read an Excel file and convert it to a CSV file
df = pd.read_excel("FinancialSample.xlsx", nrows=20)
df.to_csv("Financials.csv", index_label="Index")
