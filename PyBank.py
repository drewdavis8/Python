#import modules / dependencies
import os               
import csv

# Define PyBank's variables
months = []
profit_loss_changes = []

count_months = 0
net_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0

value =1
csv_file_path = os.path.join(".", "Resources", "budget_data.csv")
# print(csv_file_path)

output_path =  os.path.join(".", "Analysis", "budget_data.txt")

# #open and read csv
with open(csv_file_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #read the header
    csv_header = next(csv_file)
    # print(f"Header: {csv_header}")

    #Read through each row in csv file from row 2 to end
    for row in csv_reader:
        output = f"{row[0]} {row[1]}"
        # print(output)    

# Count of months
        count_months += 1

        # Net total amount of "Profit/Losses" over the entire period
        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss

        if (count_months == 1):
            # Make the value of previous month to be equal to current month
            previous_month_profit_loss = current_month_profit_loss
            continue

        else:

            # Compute change in profit loss 
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss

            # Append each month to the months[]
            months.append(row[0])

            # Append each profit_loss_change to the profit_loss_changes[]
            profit_loss_changes.append(profit_loss_change)

            # Make the current_month_loss to be previous_month_profit_loss for the next loop
            previous_month_profit_loss = current_month_profit_loss   
            #sum and average of the changes in "Profit/Losses" over the entire period
    sum_profit_loss = sum(profit_loss_changes)
    average_profit_loss = round(sum_profit_loss/(count_months - 1), 2)

    # highest and lowest changes in "Profit/Losses" over the entire period
    highest_change = max(profit_loss_changes)
    lowest_change = min(profit_loss_changes)

    # Locate the index value of highest and lowest changes in "Profit/Losses" over the entire period
    highest_month_index = profit_loss_changes.index(highest_change)
    lowest_month_index = profit_loss_changes.index(lowest_change)

    # Assign best and worst month
    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]

#  Print the analysis to the terminal
output =( "Financial Analysis\n"
"---------------------------------------------------------------------\n"
f"Total Months:  {count_months}\n"
f"Total:  ${net_profit_loss}\n"
f"Average Change:  ${average_profit_loss}\n"
f"Greatest Increase in Profits:  {best_month} (${highest_change})\n"
f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})\n")


#   Need to export to a text file with new data

print(output)
with open(output_path, "w", newline="") as textFile:
    textFile.write(output)


