import os
import csv

budget_data = os.path.join("..","Resources","budget_data.csv")

with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")
    next(csv_reader,None)
    row1 = next(csv_reader,None)
    
# Print Rows, Header
    # for row in csv_reader:
    #     print(row)

    
# Calculate Totals
    total_months = 1
    total_pl = int(0)
    month1 = int(row1[1])
    net_change = 0
    largest_increase = 0
    largest_decrease = 0
    largest_increase_row = []
    largest_decrease_row = []
    for row in csv_reader:
        total_months += 1
        total_pl = total_pl + int(row[1])
        month2 = int(row[1])
        change = month2 - month1
        if change > largest_increase:
            largest_increase = change
            largest_increase_row = [row[0],change]
        else:
            change = change
        if change < largest_decrease:
            largest_decrease = change
            largest_decrease_row = [row[0],change]
        else:
            change = change
        net_change = net_change + change
        month1 = month2

    total_pl = total_pl + int(row1[1])
    average_change = net_change / (total_months - 1)

# Print Totals
print("Financial Analysis")
print("-------------------------")
print("Total Months: ",total_months)
print("Total: ","${:,.0f}".format(total_pl))
print("Average Change: ","${:,.2f}".format(average_change))
print("Greatest Increase in Profits: ",largest_increase_row[0], "${:,.0f}".format(int(largest_increase_row[1])))
print("Greatest Decrease in Profits: ",largest_decrease_row[0], "(${:,.0f})".format(int(largest_decrease_row[1])))

budget_data_results = os.path.join("..","Analysis","budget_data_results.csv")

with open(budget_data_results,'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow(["Total Months: ",total_months])
    csvwriter.writerow(["Total: ","${:,.0f}".format(total_pl)])
    csvwriter.writerow(["Average Change: ","${:,.2f}".format(average_change)])
    csvwriter.writerow(["Greatest Increase in Profits: ",largest_increase_row[0], "${:,.0f}".format(int(largest_increase_row[1]))])
    csvwriter.writerow(["Greatest Decrease in Profits: ",largest_decrease_row[0], "(${:,.0f})".format(int(largest_decrease_row[1]))])

