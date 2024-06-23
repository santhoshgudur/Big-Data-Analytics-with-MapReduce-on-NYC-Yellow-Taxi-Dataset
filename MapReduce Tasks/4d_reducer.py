import sys

location_trip_time = {}

for line in sys.stdin:
    line = line.strip()
    pickup_location, trip_time = line.split('\t')
    trip_time = float(trip_time)

    if pickup_location in location_trip_time:
        location_trip_time[pickup_location][0] += trip_time
        location_trip_time[pickup_location][1] += 1
    else:
        location_trip_time[pickup_location] = [trip_time, 1]

for pickup_location in location_trip_time.keys():
    total_trip_time = location_trip_time[pickup_location][0]
    num_trips = location_trip_time[pickup_location][1]
    avg_trip_time = total_trip_time / num_trips
    print("The average trip time for pickup location %s is %.2f minutes" % (pickup_location, avg_trip_time))
