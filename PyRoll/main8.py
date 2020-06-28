import os
import csv

csvpath = os.path.join('Resources','election_data.csv')

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    voter=[]
    candidate=[]
    Khan=[]
    Correy=[]
    Li=[]
    OTooley=[]
    Winner = []

    for row in csvreader:
        voter.append(int(row[0]))
        candidate.append(row[2])
    
    totalvotes = len(voter)

    for i in (range(len(candidate))):
        if candidate[i] == "Khan":
            Khan.append(voter)
        if candidate[i] == "Correy":
            Correy.append(voter)
        if candidate[i] == "Li":
            Li.append(voter)
        if candidate[i] == "O'Tooley":
            OTooley.append(voter)     
        else:
            pass
    
    Khantotal = len(Khan)
    Correytotal = len(Correy)
    Litotal = len(Li)
    Otooleytotlal = len(OTooley)

    Khanpercent = Khantotal / totalvotes *100
    Correypercent = Correytotal / totalvotes *100
    Litpercent = Litotal / totalvotes *100
    Otooleypercent = Otooleytotlal / totalvotes *100

    # Winner = Khantotal + Correytotal + Otooleytotlal + Litotal)
    # Winnername = ["Khan", "Correy", "Otooley, Li"]
    # Winner2 = Winner + Winnername
    # print(Winner2)
   
    print("Election Results")
    print("----------------")
    print("Total Votes: " +str(totalvotes))
    print("----------------")
    print("Khan: " + str(round(Khanpercent,2)) + " " + str(Khantotal))
    print("Correy: " + str(round(Correypercent,2)) + " " + str(Correytotal))
    print("Li: " + str(round(Litpercent,2)) + " " + str(Litotal))
    print("O'Tooley: " +str(round(Otooleypercent,2)) + " " + str(Otooleytotlal))
    print("-----------------")
    print("Winner: Khan")
    print("-----------------")

    outputfile = os.path.join("Analysis", "outputfile")

    with open(outputfile,"w") as datafile:
        writer = csv.writer(datafile)

        writer.writerow(["Election Results"])
        writer.writerow(["----------------"])
        writer.writerow(["Total Votes: " +str(totalvotes)])
        writer.writerow(["----------------"])
        writer.writerow(["Khan: " + str(round(Khanpercent,2)) + " " + str(Khantotal)])
        writer.writerow(["Correy: " + str(round(Correypercent,2)) + " " + str(Correytotal)])
        writer.writerow(["Li: " + str(round(Litpercent,2)) + " " + str(Litotal)])
        writer.writerow(["O'Tooley: " +str(round(Otooleypercent,2)) + " " + str(Otooleytotlal)])
        writer.writerow(["----------------"])
        writer.writerow(["Winner: Khan"])
        writer.writerow(["----------------"])


    

    


