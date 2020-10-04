import os
import csv

Total_Months = 0
net_total = 0
Current_P = 0
Previous_P = 0
Pl_Change = []
P_changes = []
months = []

budget_csv = os.path.join("Resources", "budget_data.csv")
with open(budget_csv, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    for rows in csv_reader:
        P_changes.append(int(rows[1]))
        months.append(rows[0])
        net_total=net_total+int(rows[1])
    for i in range(1,len(P_changes)):
        Pl_Change.append(int(P_changes[i])-int(P_changes[i-1]))

    Total_Months = len(months)
    print("Financial Analysis")
    print("--------------------")
    print(f"Total Months: " + str(Total_Months))
    print(f"Total: " + "$" + str(net_total))
    sum_P_changes = sum(Pl_Change)
    Average_Change = round(sum_P_changes / len(Pl_Change), 2)
    print(f"Average change: " + "$" + str(Average_Change))
    greatest_increase = max(Pl_Change)
    
    greatest_decrease = min(Pl_Change)
   
    increase_date = months[Pl_Change.index(greatest_increase)+1]
    decrease_date = months[Pl_Change.index(greatest_decrease)+1]
    print(f"Greatest Increase:  {increase_date} ($  {greatest_increase})")
    print(f"Greatest Decrease:  {decrease_date} (${greatest_decrease})")
    
    output_file=os.path.join("Analysis", "financial.txt")
    file=open (output_file, "w")
    file.write ("Financial Analysis\n")
    file.write ("--------------\n")
    file.write ("Total Months:" + "$" + str(Total_Months)+"\n")
    file.write ("Total:"+ "$" + str(net_total)+"\n")
    file.write ("Average Change:" + "$" + str(Average_Change)+"\n")
    file.write ("Greatesest Increase in Profits:" + str(increase_date)+ "("+ "$" + str(greatest_increase)+")"+ "\n")
    file.write ("Greatest Decrease in Profits:" + str(decrease_date)+ "(" +  "$" + str(greatest_decrease)+")" + "\n")


    
