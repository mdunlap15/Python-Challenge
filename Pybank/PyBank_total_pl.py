import os
import csv

budget_data = os.path.join("..","PyBank","budget_data.csv")

with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")

    # csv_header = next(csv_file)
    # print(csv_header)
    
    # for row in csv_file:
    #     print(len(row))

def total_months(months):
    total = -1
    for month in months:
        total += month
    return total

print(total_months(10))

