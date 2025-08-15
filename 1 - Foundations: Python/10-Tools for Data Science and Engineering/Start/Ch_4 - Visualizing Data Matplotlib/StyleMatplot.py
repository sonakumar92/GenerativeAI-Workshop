# Example file for Advanced Python: Top Tools for Data Science
# Using the Polars library create and access a DataFrame

import matplotlib.pyplot as plt
import pandas as pd

# Create a dataset for sales data
data = {
    'Month': ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
    'SalesAmount': [1200, 800, 1400, 1500, 1900, 1500, 1300, 850, 1125, 1094, 1356, 1289],
    'Profits': [400, 200, 500, 300, -100, -200, 400, 500, 600, 450, 425, 525]
}

# Create a DataFrame from the data object
df = pd.DataFrame(data)

# Create a basic plot
# Use the subplots function to create an axes and a figure
fig, ax = plt.subplots()

# Customize the plot appearance
plt.style.use("fivethirtyeight")

# Plot the data as a line chart
# ax.plot(df['Month'], df['SalesAmount'])
# ax.plot(df['Month'], df['Profits'])

# Plot the data as a line chart with some customization
ax.plot(df['Month'], df['SalesAmount'])
ax.plot(df['Month'], df['Profits'])

# Plot the data as a bar chart with some customization
# ax.bar(df['Month'], df['SalesAmount'])
# ax.bar(df['Month'], df['Profits'])

# Set the chart properties
ax.set_title("Sales and Profits")
ax.set_xlabel("Month")
ax.set_ylabel("Amount")

#define a custom formatter for the y axis

# add the legend
ax.legend(['Sales', 'Profits'])

# add a watermark


# Show the result
plt.show()
