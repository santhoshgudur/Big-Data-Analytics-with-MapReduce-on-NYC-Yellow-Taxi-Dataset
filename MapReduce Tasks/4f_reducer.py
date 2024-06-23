import sys

time_revenue = {}

for line in sys.stdin:
    line = line.strip()
    month_year, time_of_day, day_of_week, total_amount = line.split('\t')
    total_amount = float(total_amount)

    key = "%s-%s-%s" % (month_year, time_of_day, day_of_week)
    if key in time_revenue:
        time_revenue[key][0] += total_amount
        time_revenue[key][1] += 1
    else:
        time_revenue[key] = [total_amount, 1]

for key in time_revenue.keys():
    avg_revenue = time_revenue[key][0] / time_revenue[key][1]
    print("%s\tAverage revenue: $%.2f" % (key, avg_revenue))
