from datetime import datetime

month, day, year = input().split()
month = int(month)
day = int(day)
year = int(year)
date_obj = datetime(year, month, day)

# Get the day name directly from the datetime object using strftime
day_name = date_obj.strftime("%A").upper()
print(day_name)
