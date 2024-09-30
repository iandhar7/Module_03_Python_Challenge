import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")
csv_path = "budget_data.csv"

total_months = 0
net_total = 0
changes = []
dates = []

with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        total_months += 1
        net_total += int(row[1])
        if dates:
            changes.append(int(row[1]) - prev_profit_loss)
        dates.append(row[0])
        prev_profit_loss = int(row[1])

average_change = sum(changes) / len(changes)
greatest_increase = max(changes)
greatest_decrease = min(changes)

increase_date = dates[changes.index(greatest_increase) + 1]
decrease_date = dates[changes.index(greatest_decrease) + 1]

output = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {increase_date} (${greatest_increase})
Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})
"""

print(output)

with open("Analysis/financial_analysis.txt", "w") as output_file:
    output_file.write(output)
