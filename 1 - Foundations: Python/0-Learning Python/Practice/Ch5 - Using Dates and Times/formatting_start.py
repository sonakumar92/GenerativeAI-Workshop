
#
# Example file for formatting time and date output
# LinkedIn Learning Python course by Joe Marini
#


from datetime import datetime

# Times and dates can be formatted using a set of predefined string
# control codes 
now = datetime.now() # get the current date and time


#### Date Formatting ####

# %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
# abbreviated/full year with century
print(now.strftime(f"%y, %Y")) # Output: 23, 2023
# abbreviated/full weekday name
print(now.strftime(f"%a, %A")) # Output: Thu, Thursday
# abbreviated/full month name
print(now.strftime(f"%b, %B")) # Output: Jan, January
# day of month
print(now.strftime(f"%d")) # Output: 23

# %c - locale's date and time, %x - locale's date, %X - locale's time
# Locale's date and time
print(now.strftime(f"%c")) # Output: Thu Jan 23 14:55:02 2023
# Locale's date
print(now.strftime(f"%x")) # Output: 01/23/23
# Locale's time
print(now.strftime(f"%X")) # Output: 14:55:02

#### Time Formatting ####
# %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
# 12 Hour
print(now.strftime(f"%I")) # Output: 02
# 24 Hour
print(now.strftime(f"%H")) # Output: 14
# Minute
print(now.strftime(f"%M")) # Output: 55
# Second
print(now.strftime(f"%S")) # Output: 02
# Locale's AM/PM
print(now.strftime(f"%p")) # Output: PM
