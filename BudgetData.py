print("Financial Analysis")
print("-----------------------")



import os
import csv


celllist1 = []
celllist2 = []


csvpath = os.path.join('budget_data.csv')
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        for cell in row:
            try:
                celllist1.append(int(cell))
            except ValueError:
                celllist2.append(str(cell))

print('Total Months:' + ' ' + str(len(celllist2)))
print('Total:' + ' ' + '$' + str(sum(celllist1)))



monthlychange = [y - x for x,y in zip(celllist1, celllist1[1:])]
averagechange = ("{:.2f}".format(sum(monthlychange)/len(celllist2)))
print('Average Change:' + ' ' + '$' + str(averagechange))
greatestincreaseinprofits = max(monthlychange)
greatestdecreaseinlosses = min(monthlychange)

print('Greatest Increase In Profits:' + ' ' + str(greatestincreaseinprofits))
print('Greatest Increase In Profits:' + ' ' + str(greatestdecreaseinlosses))
monthlychangecount=(1)
monthlychangecount2=(1)
answermonthlychangecount = (0)


        
                
                
                
                
                



       
        


    




 

             
          
             







