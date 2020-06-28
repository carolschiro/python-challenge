import os
import csv

csvpath = os.path.join ('Resources','budget_data.csv')

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    date=[]
    margin=[]
    monthlychange=[]

    for row in csvreader:
        date.append(row[0])
        margin.append(int(row[1]))

    total_months = len(date)
    total_profit = sum(margin)

    for i in (range(len(margin)-1)):
        monthlychange.append(margin[i+1]-margin[i])
    
    profit_avg = sum(monthlychange) / len(monthlychange)

    increase = max(monthlychange)
    decrease = min(monthlychange)

    index_monthlychange = monthlychange.index(increase)
    max_value = (monthlychange[index_monthlychange])
    max_date = (date[index_monthlychange+1])

    index_monthlychangemin = monthlychange.index(decrease)
    min_value = (monthlychange[index_monthlychangemin])
    min_date = (date[index_monthlychangemin+1])

    print("Financial Analysis")
    print("------------------")
    print("Total Months: " +str(total_months))
    print("Average Change: " + "$" + str(round(profit_avg,2)))
    print("Greatest Increase in Profits: " + str(max_date + " $" + str(max_value)))
    print("Greatest Decrease in Profits: " + str(min_date + " $" + str(min_value)))

    output_file = open("output.txt","w")
    output_file.write("Financial Analysis" + "\n")
    output_file.write("------------------" + "\n")
    output_file.write("Total Months: " + str(total_months) + "\n")
    output_file.write("Average Change: " + "$" + str(round(profit_avg,2)) + "\n")
    output_file.write("Greatest Increase in Profits: " + str(max_date + " $" + str(max_value)) + "\n")
    output_file.write("Greatest Decrease in Profits: " + str(min_date + " $" + str(min_value)) + "\n")