import os
import csv

election_csv = os.path.join('Resources', 'election_data.csv')
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")
    total_votes = 0
    khan_votes = 0
    correy_votes = 0
    Li_votes = 0
    otooley_votes = 0

    for clmns in csv_reader:
        total_votes = total_votes + 1
        if clmns [2] == "Khan":
            khan_votes = khan_votes + 1

        elif clmns [2] == "Correy":
            correy_votes = correy_votes + 1
        
        elif clmns [2] == "Li":
            Li_votes = Li_votes + 1
        
        else:
            otooley_votes = otooley_votes + 1

    khan_percent = round((khan_votes / total_votes),2)
    correy_percent = round ((correy_votes / total_votes),2)
    Li_percent = round((Li_votes / total_votes),2)
    otooley_percent = round((otooley_votes / total_votes),2)

    winner = max(khan_votes,correy_votes,Li_votes,otooley_votes)
    if winner == khan_votes:
        winner_is = "Khan"
    elif winner == correy_votes:
        winner_is = "Correy"
    elif winner == Li_votes:
        winner_is = "Li"
    else:
        winner_is = "Otooley"

    print(f"Election Results")
    print(f"-----------------")
    print(f"Total Votes: {total_votes}")
    print(f"-----------------")
    print(f"Khan: {khan_percent:.2%}")
    print(f"Correy: {correy_percent:.2%}")
    print(f"Li: {Li_percent:.2%}")
    print(f"Otooley: {otooley_percent:.2%}")
    print(f"Winner is: {winner_is}")

    output_file=os.path.join("Analysis", "Votes.txt")
    file=open (output_file, "w")
    file.write ("Election Results"+"\n")
    file.write ("--------------\n")
    file.write ("Total Votes:" + str(total_votes)+"\n")
    file.write ("--------------\n")
    file.write ("Khan:" + str(khan_percent)+"(" + str(khan_votes)+")" + "\n")
    file.write ("Correy:" + str(correy_percent)+ "("+ str(correy_votes)+")" + "\n")
    file.write ("Li:" + str(Li_percent)+ "(" + str(Li_votes)+")" + "\n")
    file.write ("O'Tooley:" + str(otooley_percent) + "(" + str(correy_votes)+")" + "\n")
    file.write ("--------------\n")
    file.write ("Winner:" + (winner_is) + "\n")
