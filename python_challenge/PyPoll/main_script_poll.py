import os
import csv

election_data = os.path.join("Resources", "election_data.csv")
csv_path = "election_data.csv"

total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        candidate = row[2]

        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1
       
        if candidates[candidate] > winner_votes:
            winner = candidate
            winner_votes = candidates[candidate]

percentage_format = "{:.3%}"
candidate_results = []
for candidate, votes in candidates.items():
    percentage = votes / total_votes
    formatted_percentage = percentage_format.format(percentage)
    candidate_results.append(f"{candidate}: {formatted_percentage} ({votes})")

output = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
{chr(10).join(candidate_results)}
-------------------------
Winner: {winner}
-------------------------
"""

print(output)

with open("Analysis/election_results.txt", "w") as output_file:
    output_file.write(output)
