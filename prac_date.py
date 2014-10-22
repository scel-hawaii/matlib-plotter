# Import Libraries
import csv
import numpy
import operator
import datetime
import matplotlib.pyplot as plt

### Test putting date into datetime format ###
# Establish variable list to hold date
t = []

# Set test date
date = "2014-06-18 12:10:09.999999-10"

# Modify date to proper string
date = date + "00"

# Print date
print(date)

# Strip time into proper format, add to list, and  print list
t.append(datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f%z"))
print(t)



### Getting the year, month, day, etc. from datetime object ###
# Test date to check
date_y = t[0].year
date_m = t[0].month
date_d = t[0].day
date_h = t[0].hour
date_mi = t[0].minute
date_s = t[0].second

print(date_y,'-',date_m,'-',date_d,' ',date_h,':',date_mi,':',date_s)



### Practice plotting with datetime objects ###
# Add two more dates
date = "2014-06-19 12:10:09.999999-1000"
t.append(datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f%z"))
print(t)
date = "2014-06-20 12:10:09.999999-1000"
t.append(datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f%z"))
print(t)

# Add random values for data
v = []
v = [1,2,1]

# Plot graph
plt.plot(t, v)
plt.title('Practice Plot with Datetime Objects')

# Save plot as jpeg
plt.savefig('prac_plot_datetime.png')
plt.show()



### UTC offset ###
# Finding UTC offset
a = t[0].tzinfo
print(a)


# Converting timedelta to hours, minutes, and seconds
t1 = datetime.timedelta(-1, 50400)

# Get days and seconds and print
days, seconds = t1.days, t1.seconds
print(days, seconds)

# Calculate hours, minutes, and seconds and print them
hours = days * 24 + seconds // 3600
minutes = (seconds % 3600) // 60
seconds = (seconds % 60)
print(hours, minutes, seconds)
