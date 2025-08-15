# Example file for Advanced Python: Top Tools for Data Science
# Using the Polars library create and access a DataFrame

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pandas as pd

# Create a dataset for sales data
data = {
    'Month': ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
    'SalesAmount': [1200, 800, 1400, 1500, 1900, 1500, 1300, 850, 1125, 1094, 1356, 1289],
    'Profits': [400, 200, 500, 300, -100, -200, 400, 500, 600, 450, 425, 525]
}

# Create a DataFrame from the data object
df = pd.DataFrame(data)

# Create a figure and axes 
fig, ax = plt.subplots()
fig.set_size_inches(12, 8)

# Customize the plot appearance
plt.style.use("fivethirtyeight")

# Plot the data as a line chart with some customization
# ax.plot(df['Month'], df['SalesAmount'], color='green', linestyle='--',marker='o',
#         markersize=10, markerfacecolor='white')
# ax.plot(df['Month'], df['Profits'])

# Plot the data as a bar chart with some customization
bars = ax.bar(df['Month'], df['SalesAmount'], edgecolor='black',linewidth=2)
ax.bar(df['Month'], df['Profits'], edgecolor='black',linewidth=2)
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 1,
            f'{height}', ha='center', va='bottom')

# Set the chart properties
ax.set_title("Sales and Profits")
ax.set_xlabel("Month")
ax.set_ylabel("Amount")

#define a custom formatter for the y axis
def currency_formatter(x, pos):
    return f'${int(x)}'

ax.yaxis.set_major_formatter(FuncFormatter(currency_formatter))

# add the legend
ax.legend(['Sales', 'Profits'])

# Add a watermark
fig.text(0.5, 0.5, 'SAMPLE DATA', fontsize=70, color='gray',
         ha='center', va='center', alpha=0.7, rotation=30)

# show the result
plt.show()
