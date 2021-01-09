#create a python script to perform the necessary analysis
#import necessary modules

from statistics import mean
import os
import csv

#calculate the total number of months included in the dataset and the net value of the entity over the time period

#read in the csv files
#use "os.path" method to ensure the delimeters are correct for all os
#create a variable to hold raw data file path

pathForRawBudgetDataFile = os.path.join("Resources", "pyBankBudgetData.csv")

#open the raw data file in "read" mode and create a variable to hold the data
#remember to close the file when you're done to free up any system resources used by it

rawDataFile= open(pathForRawBudgetDataFile, "r")

#use .reader to read raw data file

csvreader=csv.reader(rawDataFile) #delimiter default is ","

#use the "next" command to skip over the header row

header=next(csvreader)

#create empty lists to hold the months in column "a" and the profits and losses in column "b"

months = []
netValue = []

#iterate through columns "a" and "b" in the csvreader object and populate the lists using a "for" loop

for row in csvreader:
    months.append(row[0])
    netValue.append(int(row[1]))

#using the "len()" function, determine the total number of months in the time period by calculating the length of the "months" list and create a variable to hold the data

totalMonths = len(months)

#using the "sum()" function, determine the net profit/loss of the entire time period

netProfit = sum(netValue)

#"totalMonths" and "netProfit" now contain the requested information related to the total number of months included in the dataset and the net toatal amount of "P/L" over the entire period in the data set

#calculate the changes in P/L over the entire period, then find the average of those changes
#create an empty list to hold the values related to the changes in P/L

difference = []

#iterate through the profits and losses, now contained in the list created above named "netValue"
#subtract the value of month "i+1" from the value of month "i"
#the items in the list have to be converted to integers so the arithmetic can be completed (done above when creating the list)
#iterating through the list itself will give an error because the loop will try to subtract an iterant at the end that doesn't exist, to avoid, iterate through a range equal to the length of the list less one because Python is a "0" index language

for i in range(len(netValue)-1):
    difference.append(netValue[i+1]-netValue[i])

#calculate the average of the integers in the list of changes

averageChange=mean(difference)

#format the average so it only shows two decimal places

formattedaverageChange=format(averageChange, ",.2f")

#Calculate the greatest increase and decrease in profits/losses over the entire time period, also note the months related to the change
#create a dictionary containing the months in the dataset as the "keys" and the change in P/L as the "values"
#previously created list "months" contains the months and previously created list "difference" contains the changes each month
#remove the first month from the "months" list as there is no change in that month

del months[0]

#zip the two lists together to create the desired dictionary and find the month with the greatest increase based on the items in the dictionary

datesDifferenceDict = dict(zip(months, difference))
maxIncrease = max(datesDifferenceDict, key=datesDifferenceDict.get)

#format

maxIncreaseToPrint=(maxIncrease, "${:,.2f}".format(datesDifferenceDict[maxIncrease]))

#find the month with the greatest decrease based on the items in the dictionary

maxDecrease = min(datesDifferenceDict, key=datesDifferenceDict.get)

#format

maxDecreaseToPrint = (maxDecrease, "${:,.2f}".format(datesDifferenceDict[maxDecrease]))

#print results to terminal

pyBankFString = f"Financial Analysis\n----------------------------\nTotal Months: {totalMonths}\nTotal Profit (or Loss): ${netProfit}\nAverage  Change: ${formattedaverageChange}\nGreatest Increase in Profits: {maxIncreaseToPrint}\nGreatest Decrease in Profits: {maxDecreaseToPrint}"
print(pyBankFString)

#close the file

rawDataFile.close()

#write to a text file

#Specify the file to write to

output_path = os.path.join("Analysis", "pyBankOutputFile.txt")

#Open the file using "write" mode, then specify a variable to hold the contents

pyBankOutputFile = open(output_path, 'w')
pyBankOutputFile.write(pyBankFString)

#close the file

pyBankOutputFile.close()




