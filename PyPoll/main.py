#Dependencies 

import os
import csv

# Load CSV
pypoll_info = os.path.join ("Resources", "election_data.csv")

# Create list for each variable that will be used for results
count = 0
candidates = []
percent_votes = []
num_votes = []
candidate_unique = []

# Set up for loop to gather info needed from CSV file
with open(pypoll_info, newline="" ) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    
    header = next(csvreader)

    for row in csvreader:
        count = count + 1
        candidates.append(row[2])
    for x in set (candidates):
        candidate_unique.append(x)
        y = candidates.count(x)
        num_votes.append(y)
        z = (y/count) * 100
        percent_votes.append(z)
    
    winner_count = max(num_votes)
    winner = candidate_unique [num_votes.index(winner_count)]

#Print results
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(candidate_unique)):
            print(candidate_unique[i] + ": " + str(percent_votes[i]) +"% (" + str(num_votes[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)


#txt file creation
with open('pypoll_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(candidate_unique))):
        text.write(candidate_unique[i] + ": " + str(percent_votes[i]) +"% (" + str(num_votes[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")



