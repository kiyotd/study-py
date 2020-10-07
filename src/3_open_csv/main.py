import csv

with open('data.csv', 'r') as f:
    reader = csv.reader(f)

    for row in reader:

        if int(row[0]) >= 20:
            print(row[1])
