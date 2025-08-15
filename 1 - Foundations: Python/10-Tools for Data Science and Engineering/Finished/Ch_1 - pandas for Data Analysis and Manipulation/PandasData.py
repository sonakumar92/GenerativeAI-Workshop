# Example file for Advanced Python: Top Tools for Data Science
# Performing Pandas data operations on a DataFrame


import pandas as pd


# Create a DataFrame from the sales data CSV file
df = pd.read_csv("sales_data.csv")


# Sorting data by SalesAmount in descending order
# df = df.sort_values(by=['Product','SalesAmount'], ascending=[True,False])
# print(df)


# Filtering data for a specific region
# df = df[df['Region'] == 'North']
# print(df)


# Filtering using calculated values
# mean_val = df['SalesAmount'].mean()
# df = df[df['SalesAmount'] > mean_val]
# print(df)


# Filtering using the isin() function
# df = df[df['Quarter'].isin(['Q1','Q3'])]
# print(df)


# Filtering with the query function
# mean_val = df['SalesAmount'].mean()
# df = df.query("SalesAmount > @mean_val and Region != 'North'")
# print(df)


# Grouping data by Product and calculating total sales
# group_results = df.groupby('Product')
# print(group_results['SalesAmount'].sum())
# print(group_results['SalesAmount'].mean())
# print(group_results['SalesAmount'].max())
