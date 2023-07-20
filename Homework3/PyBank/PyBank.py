import os
import csv

budget_csv = os.path.join('Resources', 'budget_data.csv')


months = []
profit_loss_changes = []

month_count = 0
net_profit = 0
current_month_loss = 0
previous_month_loss = 0
profit_loss_change = 0

with open(budget_csv, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    for row in csv_reader:
        month_count += 1
        current_month_loss = int(row[1])
        net_profit += current_month_loss

        if (month_count == 1):
            previous_month_loss = current_month_loss
            continue

        else:
            profit_loss_change = current_month_loss - previous_month_loss
            months.append(row[0])
            profit_loss_changes.append(profit_loss_change)
            previous_month_loss = current_month_loss

    sum_profit_loss = sum(profit_loss_changes)
    average_profit_loss =round(sum_profit_loss/(month_count - 1), 2)

    highest_change = max(profit_loss_changes)
    lowest_change = min(profit_loss_changes)

    highest_month_index = profit_loss_changes.index(highest_change)
    lowest_month_index = profit_loss_changes.index(lowest_change)

    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]

print("Financial Analysis")
print("----------------")
print(f"Total Months: {month_count}")
print(f"Total: ${net_profit}")
print(f"Average Change: ${average_profit_loss}")
print(f"Greatest Increase in profits: {best_month} (${highest_change})")
print(f"Greatest Decrease in profits: {worst_month} (${lowest_change})")


budget_txtfile = os.path.join("budget_data.txt")
with open(budget_txtfile, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------\n")
    outfile.write(f"Total Months:  {month_count}\n")
    outfile.write(f"Total:  ${net_profit}\n")
    outfile.write(f"Average Change:  ${average_profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits:  {best_month} (${highest_change})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})\n")      
            

