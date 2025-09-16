#
# Example file for working with date information
#


from datetime import date
from datetime import datetime

## DATE OBJECTS
# Get today's date from the simple today() method from the date class
date = date.today()
print ("Today's date is ", date)
# Output: Today's date is  YYYY-MM-DD

# print out the date's individual components
print("Year:", date.year) # Output: Year: YYYY
print("Month:", date.month) # Output: Month: MM
print("Day:", date.day) # Output: Day: DD

# retrieve today's weekday (0=Monday, 1=Tuesday, 2=Wednesday, 3=Thursday, 4=Friday, 5=Saturday, 6=Sunday)
print("Weekday:", date.weekday()) # Output: Weekday: D

## DATETIME OBJECTS
# Get today's date from the datetime class
now = datetime.now()
print("Today's date is ", now) # Output: Today's date is  YYYY-MM-DD HH:MM:SS.mmmmmm

# Get the current time
print("Current time is ", now.strftime("%H:%M:%S")) # Output: Current time is  HH:MM:SS
