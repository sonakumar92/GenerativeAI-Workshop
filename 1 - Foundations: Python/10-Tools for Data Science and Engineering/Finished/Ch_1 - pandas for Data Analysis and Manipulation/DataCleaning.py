# Example file for Advanced Python: Top Tools for Data Science
# Performing Pandas data cleaning operations on a data set

import pandas as pd


# Sample data with issues
data = {'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'David', 'Eve', 'Bob'],
        'Age': [25, '30', 28, 25, '22', None, 30],
        'City': ['  New York', 'London ', 'paris', 'new York', ' london', '  ', 'london'],
        'Salary': [60000, 70000, 65000, 60000, 55000, 75000, 70000],
        'Date': ['2023-01-15', '2023-02-20', '2023/03/10', '2023-01-15', '2023-04-05', 'invalid', '2023-02-20']}
df = pd.DataFrame(data)

print("Original DataFrame:\n", df)

# Handling Missing Values
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')  # Convert to numeric, NaN for errors
df['Age'] = df['Age'].fillna(df['Age'].mean()) # Fill NaN with mean age
df['Date'] = pd.to_datetime(df['Date'], format="mixed", errors='coerce') # Convert to datetime, NaT for errors
# df['Date'] = df['Date'].fillna(df['Date'].min())

# String Manipulation and Inconsistent Formatting
df['City'] = df['City'].str.strip().str.title() # Remove whitespace and capitalize

# Removing Duplicates
df = df.drop_duplicates()
df = df.dropna()

print("\nCleaned DataFrame:\n", df)
