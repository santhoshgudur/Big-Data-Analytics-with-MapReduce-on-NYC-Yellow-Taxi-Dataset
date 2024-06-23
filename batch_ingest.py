import happybase
import pandas
import csv

# create connection
connection = happybase.Connection('localhost', port=9090, autoconnect=False)

# open connection to perform operations


def open_connection():
    connection.open()

# close the opened connection


def close_connection():
    connection.close()

# get the pointer to a table


def get_table(name):
    open_connection()
    table = connection.table(name)
    batch = table.batch(batch_size=10000)
    close_connection()
    return table, batch

# batch insert data in events table


def batch_insert_data(filename):
    print("starting batch insert of events")
    file = open(filename, "r")
    csv_reader = csv.reader(file)
    column_names = ["VendorID", "tpep_pickup_datetime", "tpep_dropoff_datetime", "passenger_count", "trip_distance", "RatecodeID", "store_and_fwd_flag",  "PULocationID",
                    "DOLocationID", "payment_type", "fare_amount", "extra", "mta_tax",  "tip_amount", "tolls_amount", "improvement_surcharge", "total_amount", "Airport_fee"]
    table, batch = get_table(filename)
    open_connection()
    i = 0
    for row in csv_reader:
        if i != 0:
            # temp = line.strip().split(",")
            columns = {}
            for j in range(1, len(column_names)):
                columns['info:'+column_names[j]] = row[j]
            # this put() will result in two mutations (two cells)
            batch.put(row[0], columns)
        i += 1
    batch.send()
    file.close()
    print("batch insert done")
    close_connection()


batch_insert_data('yellow_tripdata_2017-03.csv')
batch_insert_data('yellow_tripdata_2017-04.csv')
