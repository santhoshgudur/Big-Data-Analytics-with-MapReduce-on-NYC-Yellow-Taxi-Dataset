import sys

location_ratio = {}

for line in sys.stdin:
    line = line.strip()
    pickup_location, values = line.split('\t')
    ratio, count = values.split(',')
    ratio = float(ratio)
    count = int(count)

    if pickup_location in location_ratio:
        location_ratio[pickup_location][0] += ratio
        location_ratio[pickup_location][1] += count
    else:
        location_ratio[pickup_location] = [ratio, count]

# Sort pickup locations by average ratio in descending order
for pickup_location, values in sorted(location_ratio.items(), key=lambda x: x[1][0]/x[1][1], reverse=True):
    ratio = values[0] / values[1]

    # Output pickup location and average ratio if ratio is not 0
    if ratio > 0:
        print("Pickup Location:%s\tAverage ratio: %.2f" % (pickup_location, ratio))
