import sys

pickup_location_revenue = {}

for line in sys.stdin:
    line = line.strip()
    pickup_location, total_amount = line.split('\t')
    total_amount = float(total_amount)

    if pickup_location in pickup_location_revenue:
        pickup_location_revenue[pickup_location] += total_amount
    else:
        pickup_location_revenue[pickup_location] = total_amount

# Sort the pickup location revenues by value in descending order
sorted_revenues = sorted(pickup_location_revenue.items(), key=lambda x: x[1], reverse=True)

for pickup_location, revenue in sorted_revenues:
    print(f"Pickup location id:{pickup_location}  Revenue:{revenue:.2f}")
