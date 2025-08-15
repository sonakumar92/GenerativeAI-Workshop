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

# 1. Handling Missing Values

# 2. String Manipulation and Inconsistent Formatting

# 3. Removing Duplicates and Dropping NA Values
