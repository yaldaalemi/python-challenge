import os
import csv
csvpath = os.path.join('Resources','election_data.csv')
txtpath = os.path.join('Analysis','Results.txt')
RowNum = 0
name= "Charles Casper Stockham"
names=["Charles Casper Stockham"]
candids = {}
total = 0
first = 0
second = 0
third = 0
with open(txtpath, 'w') as text:
    with open(csvpath, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        csv_header = next(csvreader)
        for row in csvreader:
            if row[2] != name:
                name = row[2]
                if name not in names:
                    names.append(name)
            if row[2] == "Charles Casper Stockham":
                first = first+1
            if row[2] == "Diana DeGette":
                second = second+1
            if row[2] == "Raymon Anthony Doane":
                third = third+1
            RowNum +=1
        print(f'Total Votes:{RowNum}')
        text.write(f'Election Results\nTotal Votes:{RowNum}\n')
        sum = first+second+third
        def percent(x):
            a = x/sum*100
            return round(a,3)
        firstp = percent(first)
        secondp = percent(second)
        thirdp = percent(third)
        if first> second and first> third:
            winner  = "Charles Casper Stockham"
        if second> first and second> third:
            winner = "Diana DeGette"
        if third>first and third>second:
            winner = "Raymon Anthony Doane"
        print(f'Charles Casper Stockham: {firstp}%, ({first})')
        print(f'Diana DeGette: {secondp}%, ({second})')
        print(f'Raymon Anthony Doane: {thirdp}%, ({third})')
        print(f'Winner: {winner}')
        text.write(f'Charles Casper Stockham: {firstp}%, ({first})\nDiana DeGette: {secondp}%, ({second})\nRaymon Anthony Doane: {thirdp}%, ({third})\n')
        text.write(f'Winner: {winner}')







            
        
        

               
        

