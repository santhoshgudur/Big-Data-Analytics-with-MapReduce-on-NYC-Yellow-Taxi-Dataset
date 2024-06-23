import sys

time_revenue = {}

# Set up default values in time_revenue dictionary for each month/year combination
for month in range(1, 13):
    for year in range(2017, 2021):
        for time_of_day in ["day", "night"]:
            for day_of_week in ["weekday", "weekend"]:
                key = "%d-%d-%s-%s" % (month, year, time_of_day, day_of_week)
                time_revenue[key] = [0.0, 0]

for line in sys.stdin:
    line = line.strip()
    month_year, time_of_day, day_of_week, total_amount = line.split('\t')
    total_amount = float(total_amount)

    key = "%s-%s-%s" % (month_year, time_of_day, day_of_week)
    time_revenue[key][0] += total_amount
    time_revenue[key][1] += 1

for key in time_revenue.keys():
    if time_revenue[key][1] > 0:
        avg_revenue = time_revenue[key][0] / time_revenue[key][1]
        if avg_revenue > 0:
            print("%s\tAverage revenue: $%.2f" % (key, avg_revenue))
