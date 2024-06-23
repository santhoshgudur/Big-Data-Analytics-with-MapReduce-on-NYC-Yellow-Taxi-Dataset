import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split(',')

    # Skip the header row
    if line[0] != "VendorID":
        pickup_location = line[7]
        total_amount = line[-3]

        

        # Emit a key-value pair for the pickup location and the total amount
        print(f"{pickup_location}\t{total_amount}")
