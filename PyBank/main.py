import os
import csv
csvpath = os.path.join('Resources','budget_data.csv')
txtpath = os.path.join('Analysis','Results.txt')
RowNum = 0
total = 0
changes = []
csvdates=[]
a = 1088983
total_change = 0
changes_overtime = {"date","amount of change"}
with open(txtpath, 'w') as text:
    with open(csvpath, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        csv_header = next(csvreader)
        for row in csvreader:
            RowNum +=1
            total = total + int(row[1])
            # csvdates.append(row[0])
        print(f'Total Months:{RowNum}')
        print(f'Total: {total}')
        text.write(f'Total Months:{RowNum}\n')
        text.write(f'Total: {total}\n')
        with open(csvpath, 'r') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            csv_header = next(csvreader)
            first_column = next(csvreader)
            for row in csvreader:
                csvdates.append(row[0])
                b = int(row[1])
                change = b-a
                changes.append(change)
                a = int(row[1])
            for change in changes:
                total_change = total_change + change
                minimum = min(changes)
                maximum = max(changes) 
            avg_change = total_change/85
        print(f'Average Change: {round(avg_change,2)}')
        text.write(f'Average Change: {round(avg_change,2)}\n')
    with open(csvpath, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        new_list = zip(csvdates, changes)
        for row in new_list:
            changes_overtime = {
                "date":row[0],
                "amount of change":row[1]
            }
            print(changes_overtime)
            text.write(f'{changes_overtime}\n')
    with open(csvpath, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        new_list = zip(csvdates, changes)
        for row in new_list:
            if row[1] == maximum:
                print(f'Greatest increase in profits:{row}')
                text.write(f'Greatest increase in profits:{row}\n')
            if row[1] == minimum:
                print(f'Greatest decrease in profits:{row}')
                text.write(f'Greatest decrease in profits:{row}\n')

    
  

