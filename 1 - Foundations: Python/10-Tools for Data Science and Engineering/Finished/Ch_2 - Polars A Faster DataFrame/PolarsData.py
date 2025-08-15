# Example file for Advanced Python: Top Tools for Data Science
# Using the Polars library to manipulate data within a DataFrame

import polars as pl


df = pl.read_csv("sales_data.csv")


# Sorting data
# sorted_df = df.sort("SalesAmount", descending=True)
# print(sorted_df)

# multisort_df = df.sort(["Product", "SalesAmount"], descending=[True, True])
# print(multisort_df)


# Filtering data
# filtered = df.filter(pl.col("Region") == "North")
# print(filtered)

# mean_val = pl.col("SalesAmount").mean()
# filtered = df.filter(pl.col("SalesAmount") > mean_val)
# print(filtered)

filtered = df.filter(pl.col("Quarter").is_in(["Q1","Q2"]))
print(filtered)


# Use SQL to query the DataFrame directly within Polars
# amount = 850
# result = df.sql(f"""
# 	SELECT Product, SalesAmount
# 	FROM self
#     WHERE SalesAmount >= {amount}
# 	""")
# print(result)


# Grouping data and aggregation
result = df.group_by(pl.col("Product")).agg(
    pl.col("SalesAmount").sum().alias("Total Sales"),
    pl.col("SalesAmount").mean().alias("Average Sale"),
    pl.col("SalesAmount").max().alias("Largest Sale")
)
print(result)
