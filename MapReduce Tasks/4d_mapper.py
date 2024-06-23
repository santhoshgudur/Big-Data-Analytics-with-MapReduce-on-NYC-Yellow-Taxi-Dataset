import sys
from datetime import datetime

for line in sys.stdin:
    line = line.strip()
    line = line.split(',')

    if line[0] != "VendorID":
        pickup_location = line[7]
        pickup_time = line[1]
        dropoff_time = line[2]

        # Parse pickup_time and dropoff_time into datetime objects
        pickup_time = datetime.strptime(pickup_time, '%m-%d-%Y %H:%M')
        dropoff_time = datetime.strptime(dropoff_time, '%m-%d-%Y %H:%M')

        # Calculate trip time in minutes
        trip_time = (dropoff_time - pickup_time).total_seconds() / 60

        print('%s\t%s' % (pickup_location, trip_time))
