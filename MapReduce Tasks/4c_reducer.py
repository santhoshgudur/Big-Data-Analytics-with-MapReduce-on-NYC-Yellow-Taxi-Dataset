import sys

payment_type_count = {}

for line in sys.stdin:
    line = line.strip()
    payment_type, count = line.split('\t')
    count = int(count)

    if payment_type in payment_type_count:
        payment_type_count[payment_type] += count
    else:
        payment_type_count[payment_type] = count

# Sort the payment type counts by value in descending order
sorted_counts = sorted(payment_type_count.items(), key=lambda x: x[1], reverse=True)

for payment_type, count in sorted_counts:
    print("Payment_Type:%s Count=%d" % (payment_type, count))
