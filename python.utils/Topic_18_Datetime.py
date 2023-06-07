from datetime import datetime


import datetime

# Get current time
x = datetime.datetime.now()
print(x)

# get the year or month 
print(x.year)
print(x.month)
print(x.day)

# get the current time by format
print(x.strftime("%Y-%m-%d"))

# create a date object
y = datetime.datetime(2023, 6, 5)
z = datetime.datetime(x.year, x.month, x.day, x.hour - 1, x.minute -2 , x.second - 1)

# canculate the distance of 2 date object
print(x-y)
print(x-z)
