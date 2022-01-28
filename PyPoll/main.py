import os
import csv

pypoll_info = os.path.join ("..", "Resources", "election_data.csv")
results = os.path.join("..", "Analysis", "PyPoll_results.txt")

# Create list for each variable that will be used for results
vote_sum = 0
candidates = []
percent_votes = []
num_votes = []
winner = 0

#total votes
with open(pypoll_info,'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    
    header = next(reader)

    for row in reader:
        vote_sum += 1
    if row[2] not in candidates:
        candidates.append(row[2])
        num_votes.append(1)
    else:
        candidate_index = candidates.index(row[2])
        num_votes[candidate_index] +=1
# % calculation
for i in range(len(num_votes)):
    percent_votes.append(num_votes[i] / vote_sum)

#winner
for i in range(len(num_votes)):
    if num_votes[i] > winner:
        winner = num_votes[i]
        winner_name = candidates [i]


#txt file
with open(results, 'w') as txtfile:
    txtfile.f.write(print(f"Election Results"
                        f"--------------------------"
                        f"Total Votes: {str(vote_sum)}"
                        f"--------------------------")
                        )
    for i in range (len(candidates)):
        txtfile.write(print("{candidate[i]}: {percent_votes[i]}" " ({num_votes[i]}"))

        txtfile.write(print("-----------------------"
                            "Winner: {winner}"
                            "-----------------------")
                            )

with open (results, 'r') as analysis:
        result_values = analysis.read()
        print(result_values)



