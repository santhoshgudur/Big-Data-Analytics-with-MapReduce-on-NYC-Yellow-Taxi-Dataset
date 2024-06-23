import sys

vendor_trips = {}

for line in sys.stdin:
    # Split the input line into a key and a value
    key, value = line.strip().split('\t')

    # Convert the value to a float
    value = float(value)

    if key in vendor_trips:
        # Update the total revenue for the vendor
        vendor_trips[key] += value
    else:
        # Initialize the total revenue for the vendor
        vendor_trips[key] = value

# Find the vendor with the most trips
most_trips_vendor = max(vendor_trips, key=vendor_trips.get)

# Print the vendor ID and the total revenue for the vendor with the most trips
print(f"Vendor ID: {most_trips_vendor}\nTotal Revenue: {vendor_trips[most_trips_vendor]}")
