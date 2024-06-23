import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split(',')

    # Skip first line of input data
    if fields[0] != "VendorID":
        vendor_id, pickup_datetime, dropoff_datetime, passenger_count, trip_distance, rate_code, store_and_fwd_flag, pickup_location_id, dropoff_location_id, payment_type, fare_amount, extra, mta_tax, tip_amount, tolls_amount, improvement_surcharge, total_amount, congestion_surcharge, airport_fee = fields

        # Convert tip amount and total amount to floats
        tip_amount = float(tip_amount)
        total_amount = float(total_amount)

        # Calculate tips to revenue ratio
        if total_amount > 0:
            ratio = tip_amount / total_amount
        else:
            ratio = 0

        # Output key-value pair with pickup location as key and (ratio, 1) as value
        print("%s\t%.2f,1" % (pickup_location_id, ratio))
