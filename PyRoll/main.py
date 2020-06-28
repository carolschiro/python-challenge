import os
import csv

csvpath = os.path.join ('Resources','election_data.csv')

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    voter = []
    canidate = []
    total_canidate =[]

    for row in csvreader:
        voter.append(int(row[0]))
        canidate.append(row[2])
    total_votes = len(voter)
    print(total_votes)

    for i in canidate:
        total_canidate.append(sum(canidate[i])
    