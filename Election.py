
# coding: utf-8

# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

# In[1]:


import csv
import os

fname = os.path.join('Resources', 'election_data.csv')

with open(fname, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)

   #total number of votes casted
    total_voters = 0
   #complete list of candidates per vote
    list_candidates = []
   #votes for each candidate
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0

    for i in csvreader:
        total_voters +=1
        list_candidates.append(i['Candidate'])

        if i["Candidate"].lower() == "khan":
            khan_votes += 1
        elif i["Candidate"].lower() == "correy":
            correy_votes +=1
        elif i["Candidate"].lower() == "li":
            li_votes +=1
        elif i["Candidate"].lower() == "o'tooley":
            otooley_votes += 1

        if khan_votes > correy_votes or li_votes or otooley_votes:
            winner = "Khan"
        elif correy_votes > khan_votes or li_votes or otooley_votes:
            winner = "Correy"
        elif li_votes > khan_votes or correy_votes or otooley_votes:
            winner = "Li"
        elif otooley_votes > khan_votes or correy_votes or li_votes:
            winner = "O'Tooley"

        #candidate percentages
    k_perc = (khan_votes/total_voters) * 100
    c_perc = (correy_votes/total_voters) * 100
    l_perc = (li_votes/total_voters) * 100
    o_perc = (otooley_votes/total_voters) * 100

    print("Election Results")
    print("-------------------------------------------")
    print(f"Total Votes: {total_voters}")
    print("-------------------------------------------")
    print(f"Khan: {round(k_perc,2)}00% ({khan_votes})")
    print(f"Correy: {round(c_perc,2)}00% ({correy_votes})")
    print(f"Li: {round(l_perc,2)}00% ({li_votes})")
    print(f"O'Tooley: {round(o_perc,2)}00% ({otooley_votes})")
    print("-------------------------------------------")
    print(f"Winner: {winner}")
    print("-------------------------------------------")

with open('election_results.txt', 'w') as wf:

    wf.write("Election Results\n")
    wf.write("-------------------------------------------\n")
    wf.write(f"Total Votes: {total_voters}\n")
    wf.write("-------------------------------------------\n")
    wf.write(f"Khan: {round(k_perc,2)}00% ({khan_votes})\n")
    wf.write(f"Correy: {round(c_perc,2)}00% ({correy_votes})\n")
    wf.write(f"Li: {round(l_perc,2)}00% ({li_votes})\n")
    wf.write(f"O'Tooley: {round(o_perc,2)}00% ({otooley_votes})\n")
    wf.write("-------------------------------------------\n")
    wf.write(f"Winner: {winner}\n")
    wf.write("-------------------------------------------\n")

