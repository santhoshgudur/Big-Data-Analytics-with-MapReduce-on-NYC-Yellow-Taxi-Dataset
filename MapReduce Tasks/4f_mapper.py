import sys
from datetime import datetime

for line in sys.stdin:
    line = line.strip()
    line = line.split(',')

    if line[0] != "VendorID":
        pickup_time = line[1]
        total_amount = float(line[-3])

        # Parse pickup_time into a datetime object
        pickup_time = datetime.strptime(pickup_time, '%m-%d-%Y %H:%M')

        # Get the month and year of the pickup time
        month = pickup_time.month
        year = pickup_time.year

        # Get the hour of the pickup time
        hour = pickup_time.hour

        # Determine if pickup time is during the day or night
        if hour >= 8 and hour < 20:
            time_of_day = "day"
        else:
            time_of_day = "night"

        # Determine if pickup time is on a weekday or weekend
        if pickup_time.weekday() < 5:
            day_of_week = "weekday"
        else:
            day_of_week = "weekend"

        print("%s-%s\t%s\t%s\t%s" % (month, year, time_of_day, day_of_week, total_amount))
