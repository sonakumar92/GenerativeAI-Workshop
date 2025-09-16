#
# Example file for working with timedelta objects
# The purpose of timedelta is simple:
# It lets you represent and work with durations of time (like “5 minutes”, “2 days”, “3 weeks”) so you can do calculations with dates and times.
# Without timedelta, you’d have to manually add seconds or worry about things like month boundaries, leap years, etc. timedelta handles that math for you.
# Why it’s useful:
# Add/Subtract time easily
# → move forward or backward from a given date (today + 30 days).
# Find differences
# → how many days between two dates (date2 - date1).
# Control expiry
# → sessions, JWT tokens, cache timeouts, etc.
# Scheduling
# → repeat something every X days/hours.
#


from datetime import date
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
delta = timedelta(days=5, hours=3, minutes=30)
print(delta) # Output: 5 days, 3:30:00

# print today's date
today = date.today()
print(today) # Output: 2023-01-23

# print today's date one year from now
print(today + timedelta(days=365)) # Output: 2024-01-23

# create a timedelta that uses more than one argument
print(timedelta(weeks=2, days=5, hours=3, minutes=30)) # Output: 19 days, 3:30:00

# calculate the date 1 week ago, formatted as a string
print((today - timedelta(weeks=1)).strftime("%Y-%m-%d")) # Output: 2023-01-16

### How many days until April Fools' Day?
april_fools = date(today.year, 4, 1)
if april_fools < today:
    april_fools = date(today.year + 1, 4, 1)
days_until = (april_fools - today).days
print(f"Days until April Fools' Day: {days_until}")