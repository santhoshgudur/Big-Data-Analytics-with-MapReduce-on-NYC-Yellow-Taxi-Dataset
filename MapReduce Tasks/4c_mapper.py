import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split(',')

    if line[0] != "VendorID":
        payment_type = line[9]

        print('%s\t1' % payment_type)
