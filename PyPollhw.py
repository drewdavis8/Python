#declare and initiate variables
import csv
import os

#declare totals variables
total = 0
total_votes = 0
total_month_avg_denom = 0


#declare to hold change values
max_increase = 0
max_decrease = 0

candidate_dict = dict()

csv_file_path = os.path.join(".", "election_data.csv")
# print(csv_file_path)

output_path =  os.path.join(".", "Analysis", "election-data.txt")

with open(csv_file_path,'r') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter = ',')
    next(csv_reader)

    #Read in file and loop through
    for row in csv_reader:        
       total_votes += 1

       if row[2] in candidate_dict:
            candidate_dict[row[2]] += 1
       else: 
            candidate_dict[row[2]] = 1

    winner = max(candidate_dict, key=candidate_dict.get)


#create an output  LOLZ
output = (    
    f"\nElection Results\n"
    f"-----------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-----------------------\n\n"
)
for candidate in candidate_dict:
    output += f"{candidate}: {(candidate_dict.get(candidate)/total_votes)*100: .3f}% ({candidate_dict.get(candidate)}) \n"

output += ( 
    f"\n-----------------------\n"
    f"Winner: {winner}\n"
    f"-----------------------"
    )


#print to screen and file

print(output)
with open(output_path, "w", newline="") as output_file:
    output_file.write(output)