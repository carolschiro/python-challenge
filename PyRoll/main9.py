import os
import csv

csvpath = os.path.join ('Resources','election_data.csv')

voter = []
county = []
canidate = []
canidate_count =[]

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        voter.append(int(row[0]))
        canidate.append(row[2])

    for i in canidate:
        canidate_count.append(int(len(voter[i])))
        print(canidate_count)
        break
    
    
    # for i in (range(len(canidate))):
    #     print(i)
    #     break