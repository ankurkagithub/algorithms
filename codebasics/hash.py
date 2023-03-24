import csv

with open("./hash.csv","r") as file:
    data = csv.reader(file)
    for row in data:
        print(row)
