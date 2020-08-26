import os
import csv

election_data = os.path.join("..","Resources","election_data.csv")

with open(election_data) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")
    next(csv_reader,None)

# Check that there are not duplicate ID's
    # voter_ids = []
    # for voter in csv_reader:
    #     if voter[0] not in voter_ids:
    #         continue
    #     else:
    #         voter_ids.append(voter)
    # print(len(voter_ids))

# Check for unique candidate names
    # candidates = []
    # for voter in csv_reader:
    #     if voter[2] in candidates:
    #         continue
    #     else:
    #         candidates.append(voter[2])
    # print(candidates) 

    total_votes = 0
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0
    for voter in csv_reader:
        total_votes +=1
        if voter[2] == "Khan":
            khan_votes +=1
        elif voter[2] == "Correy":
            correy_votes +=1
        elif voter[2] == "Li":
            li_votes +=1
        else:
            otooley_votes +=1

    khan_percent = khan_votes / total_votes
    correy_percent = correy_votes / total_votes
    li_percent = li_votes / total_votes
    otooley_percent = otooley_votes / total_votes
    
    results = {"Correy" : correy_votes, "Khan": khan_votes, "O'Tooley" : otooley_votes, "Li" : li_votes}
    winner = max(results, key=results.get)        

    print("Election Results")
    print("-----------------------")
    print("Total Votes: ","{:,.0f}".format(total_votes))
    print("-----------------------")
    print("Khan:", "{:,.3%}".format(khan_percent), "({:,.0f})".format(khan_votes))
    print("Correy: ", "{:,.3%}".format(correy_percent), "({:,.0f})".format(correy_votes))
    print("Li: ", "{:,.3%}".format(li_percent), "({:,.0f})".format(li_votes))
    print("O'Tooley: ", "{:,.3%}".format(otooley_percent), "({:,.0f})".format(otooley_votes))
    print("-----------------------")
    print("Winner: ", winner)
    print("-----------------------")

election_data_results = os.path.join("..","Analysis","election_data_results.csv")

with open(election_data_results,'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-----------------------"])
    csvwriter.writerow(["Total Votes: ","{:,.0f}".format(total_votes)])
    csvwriter.writerow(["-----------------------"])
    csvwriter.writerow(["Khan:", "{:,.3%}".format(khan_percent), "{:,.0f}".format(khan_votes)])
    csvwriter.writerow(["Correy: ", "{:,.3%}".format(correy_percent), "{:,.0f}".format(correy_votes)])
    csvwriter.writerow(["Li: ", "{:,.3%}".format(li_percent), "{:,.0f}".format(li_votes)])
    csvwriter.writerow(["O'Tooley: ", "{:,.3%}".format(otooley_percent), "{:,.0f}".format(otooley_votes)])
    csvwriter.writerow(["-----------------------"])
    csvwriter.writerow(["Winner: ", winner])
    csvwriter.writerow(["-----------------------"])