import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")
budget_solved = os.path.join ("Analysis", "PyBank_result.txt")

count = 0
dates = []
profit = []
total_profit = 0
greatest_inc =0
greatest_dec = 0
initial_profit = 0
monthly_prof = []
total_change = 0

with open(budget_csv, 'r') as csv_file:
        next(csv_file)
        csv_reader = csv.reader(csv_file, delimiter=",")

        header = next(csv_reader)

        for row in csv_reader:
            count = count + 1
            dates.append(row[0])
            profit.append (int(row[1]))
            total_profit = total_profit + int(row[1])

            final_profit = int(row[1])
            monthly_profit = final_profit - initial_profit

            monthly_prof.append(monthly_profit)

            total_change = total_change + monthly_profit
            initial_profit = final_profit
            average_change = (total_change / count)
            greatest_inc = max(monthly_prof)
            greatest_dec = min(monthly_prof)
            inc_date = dates[monthly_prof.index(greatest_inc)]
            dec_date = dates[monthly_prof.index(greatest_dec)]


print("Financial Analysis")
print("Total Months: " + str(count))
print("Total Profits: " + "$" + str(total_profit))
print("Average Change: " + "$" + str(int(average_change)))
print ("Greatest Increase in Profits: " + str(inc_date) + " ($" + str(greatest_inc) + ")")
print ("Greatest Decrease in Profits: " + str(dec_date) + " ($" + str(greatest_dec) + ")")


with open('budget_solved.txt', 'w') as text:
    text.write("Financial Analysis"+ "\n")
    text.write("--------------------------\n")
    text.write("    Total Months: " + str(count) +"\n")
    text.write("    Total Profits: " + "$" + str(int(average_change)) +"\n")
    text.write("    Average Change: " + "$" + str(int(average_change)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(inc_date) + " ($" + str(greatest_inc) + "\n" )
    text.write("    Greatest Decrease in Profits: " + str(dec_date) + " ($" + str(greatest_dec) + "\n" )
