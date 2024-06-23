import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split(',')

    if line[0] != "VendorID":
        vendorid = line[0]
        total_amount = line[-1]

        print('%s\t1\t%s' % (vendorid, total_amount))
        
