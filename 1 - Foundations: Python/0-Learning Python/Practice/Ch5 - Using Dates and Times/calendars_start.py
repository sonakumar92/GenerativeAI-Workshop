#
# Example file for working with Calendars
# LinkedIn Learning Python course by Joe Marini
#


import calendar

# create a plain text calendar
# Default Start day is Monday
cal = calendar.TextCalendar()
str = cal.formatmonth(2026, 1, 0, 0)
print(str)
# Set the first weekday to Sunday
cal = calendar.TextCalendar(calendar.SUNDAY)
str = cal.formatmonth(2026, 1, 0, 0)
print(str)


# create an HTML formatted calendar
html_cal = calendar.HTMLCalendar(calendar.SUNDAY)
str = html_cal.formatmonth(2026, 1)
print(str)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for i in cal.itermonthdays(2026, 8):
    print(i)
# Output: 0 0 0 0 0 0 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31

# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
for name in calendar.month_name:
    print(name)
# Output: January February March April May June July August September October November December

for day in calendar.day_name:
    print (day)
# Output: Sunday Monday Tuesday Wednesday Thursday Friday Saturday

# Print the abbreviated month names
for name in calendar.month_abbr:
    print(name)
# Output: Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
# Print the abbreviated day names
for name in calendar.day_abbr:
    print(name)
# Output: Sun Mon Tue Wed Thu Fri Sat

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
print ("Team meetings will be on:")
for m in range(1,13):
    # returns an array of weeks that represent the month
    cal = calendar.monthcalendar(2026, m)
    # The first Friday has to be within the first two weeks
    first_friday = None
    for week in cal[:2]:
        if week[calendar.FRIDAY] != 0:
            first_friday = week[calendar.FRIDAY]
            break
    if first_friday:
        print(f"Month {m}: {first_friday}")