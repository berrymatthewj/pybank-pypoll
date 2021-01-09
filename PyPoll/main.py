#calculate the total number of votes cast

#import necessary modules

import os
import csv

#use "os.path" method to ensure the delimeters are correct for all os
#create a variable to hold raw data file path

pathForRawElectionDataFile = os.path.join("Resources", "pyPollElectionData.csv")

#open the raw data file and create a variable to hold the data

rawDataFile=open(pathForRawElectionDataFile, "r")

#use .reader to read raw data file

csvreader=csv.reader(rawDataFile) #delimiter default is ","

#set first row as "header" so it's not included in calculations

header = next(csvreader)

#create empty lists for the candidates and the votes cast

candidates = []
votesCast = []

#use a for loop to fill the empty lists

for row in csvreader:
    votesCast.append(row[0])
    candidates.append(row[2])

#use the length of the votesCast list to determine the total amount of votes cast

numVotesCast=len(votesCast)

#Create a complete list of candidates who received votes and iterate through the candidates list created above to create a dictionary containing candidates as the keywords and the amount of votes received by the candidate as the values

candidateVoteDict = {}
for i in candidates:
     if i in candidateVoteDict: candidateVoteDict[i] += 1
     else: candidateVoteDict[i] = 1
values = candidateVoteDict.values()

#use the amount of votes received by each candidate to calculate the percentage of the total vote received by each candidate

#iterate through the candidateVoteDict dictionary values and divide those numbers by the total number of votes cast to create a list of the percentage of the vote

percentageOfVote = []
for value in candidateVoteDict.values():
    percentageOfVote.append("{:.3%}".format(value/numVotesCast))

#iterate through the candidateVoteDict dictionary keywords to create a list of the individual candidates

candidatesList = []
for key in candidateVoteDict.keys():
    candidatesList.append(key)

#use the "zip" function to merge the percentageOfVote list to the candidatesList and create a dictionary with the candidates' names as the keywords and the percentage of the votes as the values

candidatesPercentageDict=dict(zip(candidatesList, percentageOfVote))

#use the "zip" function to merge the percentageOfVote list to a list of the values from the candidatesPercentageDict dictionary

numbersList = list(zip(percentageOfVote, candidateVoteDict.values()))

#use the zip function to create a dictionary with the candidates' names as the keywords and the percentage of the total vote they won, along with the total votes they received as the values

masterDict = dict(zip(candidatesList, numbersList))


#use "sorted" and "items" functions to return a list of tuples containing the candidates' names and the values of the masterDict dictionary sorted from highest to lowest

sortedMasterDict=sorted(masterDict.items(), key=lambda x: x[1], reverse=True)

#use "operator" "max", "items", and "itemgetter" to return the keyword from masterDict dicionary with the most votes and store it in the "winner" category
#import "operator"

import operator
import re
winner=max(masterDict.items(), key=operator.itemgetter(1))[0]

#print to terminal

Fstring1 = f"Election Results\n-------------------------\nTotal Votes: {numVotesCast}\n-------------------------\n"
print(Fstring1)

for name, performance in masterDict.items():
    namePerformance=str((name,performance))
    namePerformance=namePerformance.replace("(", " ")
    namePerformance=namePerformance.replace(")", " ")
    namePerformance=namePerformance.replace(",", " ")
    namePerformance=namePerformance.replace("'", " ")
    namePerformance=namePerformance.replace('"', " ")
    print(namePerformance)

Fstring2 = f"-------------------------\nWinner: {winner}\n-------------------------"
print(Fstring2)

rawDataFile.close()

#print to output file

outputPath = os.path.join("Analysis", "PyPollMainOutputFile.txt")
PyPollMainOutputFile = open(outputPath, "w")
PyPollMainOutputFile.write(Fstring1)
for name, performance in masterDict.items():
    namePerformance=str((name, performance))
    namePerformance=namePerformance.replace("(", " ")
    namePerformance=namePerformance.replace(")", " ")
    namePerformance=namePerformance.replace(",", " ")
    namePerformance=namePerformance.replace("'", " ")
    namePerformance=namePerformance.replace('"', " ")
    PyPollMainOutputFile.write(namePerformance)
    PyPollMainOutputFile.write("\n")
PyPollMainOutputFile.write(Fstring2)
rawDataFile.close()

    