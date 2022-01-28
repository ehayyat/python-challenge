import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")
budget_solved = os.path.join ("Analysis", "PyBank_result.txt")

dates = []
profitloss = []
plchanges = []
greatest_inc =0
greatest_dec = 0

with open(budget_csv, 'r') as csv_file:
        next(csv_file)
        csv_reader = csv.reader(csv_file, delimiter=",")

        header = next(reader)

        for row in reader:
            dates.append(row[0])
            profitloss.append (int(row[1]))
pltotal = 0
        
for i in profitloss:
    pltotal = i + pltotal

plchanges = profitloss[i+1] - profitloss[i] for i in range (0, len(profitloss)-1)
plchanges.insert (0,0)
average_change = sum(plchanges) / len(dates)

for i in range(len(plchanges)-1):
    if plchanges[i] < greatest_dec
        greatest_dec = plchanges [i]
    if plchanges[i] > greatest_inc
        greatest_inc = plchanges[i]
    
greatest_inc_index = plchanges.index(greatest_inc)
greatest_inc_date = dates [greatest_inc_index]
greatest_dec_index = plchanges.index(greatest_dec)
greatest_dec_date = dates [greatest_inc_index]

results = ("Financial Analysis"
            "--------------------------"
            "Total Months: {len(dates)}"
            "Total: ${pltotal}"
            "Average Change: ${average_change}"
            "Greatest Increase in Profits: {greatest_inc_index} (${greatest_inc_date})"
            "Greatest Decrease in Profits: {greatest_dec_index} (${greatest_dec_date})")

print(results)

with open(budget_solved, 'w') as textfile:
    textfile.write(results)

