import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")


total_votes = 0
candidates_unique = []
candidate_votes = []

with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        total_votes += 1
        candidate_in = (row[2])
        if candidate_in in candidates_unique:
            candidate_index = candidates_unique.index(candidate_in)
            candidate_votes[candidate_index] = candidate_votes[candidate_index] + 1
        else:
            candidates_unique.append(candidate_in)
            candidate_votes.append(1)

percentage = []
max_votes = candidate_votes[0]
max_index = 0

for x in range(len(candidates_unique)):
    vote_percentage = round(candidate_votes[x]/total_votes*100, 3)
    percentage.append(vote_percentage)
    if candidate_votes[x] > max_votes:
        max_votes = candidate_votes[x]
        max_index = x
election_winner = candidates_unique[max_index]

print("Election Results")
print("---------------------")
print(f"Total Votes: {total_votes}")
print("---------------------")
for x in range(len(candidates_unique)):
    print(f"{candidates_unique[x]} : {percentage[x]:.3f}% ({candidate_votes[x]})")
print("----------------------")
print(f"Winner: {election_winner}")
print("-----------------------")


output_file = os.path.join("election_results.txt")
with open(output_file, "w", newline="") as outfile:
    outfile.write("Election Results\n")
    outfile.write("---------------------\n")
    outfile.write(f"Total Votes: {total_votes}\n")
    outfile.write("---------------------\n")
    for x in range(len(candidates_unique)):
        outfile.write(f"{candidates_unique[x]} : {percentage[x]:.3f}% ({candidate_votes[x]})\n")
    outfile.write("----------------------\n")
    outfile.write(f"Winner: {election_winner}\n")
    outfile.write("-----------------------\n")




