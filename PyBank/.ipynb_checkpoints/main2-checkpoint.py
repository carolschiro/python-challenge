import os
import csv
csvpath = os.path.join ('Resources','budget_data.csv')

def PyBank(Pybank_data):
    date = str(Pybank_data[0])
    profit_loss = int(Pybank_data[1])  

    total_months = len(date)
    print("Total Months: " + total_months)
    
    total_profit = sum(profit_loss)
    print("Total: " + str(total_profit))

    profit_avg  = (total_profit / total_months) *100
    print("Average Change: " + str(profit_avg))

    increase = max(profit_loss)
        
    decrease = min(profit_loss)
        
    if profit_loss in csvreader == increase:
        print("Greatest Increase in Profits: " + date + profit_loss)
    
    if profit_loss in csvreader == decrease:
        print("Greatest Decrease in Profits: " + date + profit_loss)      

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    print(PyBank_data)
    
    output_file = os.path.join(..',''Analysis','budget_data2.csv')

with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)
    writer.writerows(PyBank_data)


    #total number of months included in the dataset
    #The net total amoutn of "profit/losses over the entire period"
    #The average of the changes in Profit/Loss over the entire period
    #The greatest increase in profits date and amount over the entire period
    #The greastest decrease in losses (date and amount) over the entire period