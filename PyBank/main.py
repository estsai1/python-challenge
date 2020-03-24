import os
import csv

# The goal of this assignment is to read budget_data.csv, which has two columns of data: 'Date' and 'Profit/Losses'
# Analyze the records to calculate each of the following:
    # The total number of months included in the dataset
    # The net total amount of 'Profit/Losses' over the entire period
    # The average of the changes in 'Profit/Losses' over the entire period
    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in losses (date and amount) over the entire period
# Final script should print both the analysis to the terminal and export a text file with the results.

# Path to collect data from the Resources folder
# C:\Users\tenko\Documents\GitHub\python-challenge\PyBank\Resources\budget_data.csv
# C:\Users\tenko\Documents\GitHub\python-challenge\PyBank\main.py
budget_data_csv = os.path.join('Resources','budget_data.csv')

# Can approach this problem by reading the file and adding each row to list
# Create list to store data
data = []

# Other variables needed: total months (int), net total (long), average (double)
# Variables to hold the indexes of the greatest incr in profits and greatest decr in profits
totalMonths = 0
netTotal = 0
average = 0
incrIndex = 0
decrIndex = 0

# Read in the cvs file
with open(budget_data_csv) as csvfile:

    # Split the data on the commas
    csvreader = csv.reader(csvfile, delimiter = ',')

    # Skip header
    next(csvfile)

    # # Use loop to add .csv file data to the list row-by-row
    # for row in csvreader:
    #     data.append(row)
    data = [row for row in csvreader]

# Debugging purpose: Check if rows were properly added to the list
# print(data)

# The total number of months is simply the length of the list
totalMonths = int(len(data))
# print(str(totalMonths))

# netTotal can be calculated with a loop that takes the sum of all data in column 2
# This can be accomplished with a function
def calculateNetTotal(list_data):
    total = 0
    length = len(list_data)

    for x in range(length):
        total = total + int(list_data[x][1])

    return total

netTotal = calculateNetTotal(data)
# Debugging purpose: Check that netTotal is correct
# print(netTotal)

# Write a function that will return the average change
def calculateAverageChange(list_data):
    length = len(list_data)
    # Make a new list to store each change value
    change = []

    # Use for loop to measure the change between index 0 and 1, 1 and 2, etc.
    # Last case is 85 and 86, so range needs to end at length - 1
    for x in range(length - 1):
        change.append(float(list_data[x + 1][1]) - float(list_data[x][1]))

    # Now find the sum of changes (one variable) and length of change (second variable)
    changeSum = 0
    changeLength = len(change)

    for y in range(changeLength):
        changeSum = changeSum + change[y]
    
    # Return the average change i.e. changeSum / changeLength
    return changeSum / changeLength

average = calculateAverageChange(data)
# The function round(x,y) rounds number x to y decimal places, will use this to display the value correctly at the end
# print(round(average,2))

# Write a function that will find the index of the greatest increase in profits
def getGreatestIncr(list_data):

    # Will need one variable that holds the index value corresponding to the greatest increase in profits
    index = 0
    # Another variable will be initialized to the first entry in list_data
    greatest = float(list_data[0][1])
    
    # Use for loop to find the greatest increase. Start at 1, end at len(list_data),
    # if list_data[i][1] - list_data[i-1][1] is greater, reassign index and greatest
    for i in range(1, len(list_data)):
        change = float(list_data[i][1]) - float(list_data[i - 1][1])
        if change > greatest:
            greatest = change
            index = i
    
    return index

# temp = getGreatestIncr(data)
# print(temp)
# print(data[temp])
incrIndex = getGreatestIncr(data)

# Write a function to return the index of the greatest decrease in profits. Logic is similar to greatest increase
def getGreatestDecr(list_data):

    index = 0
    greatest = float(list_data[0][1])

    # This time check for change smaller than greatest with a conditional for loop
    for j in range(1, len(list_data)):
        change = float(list_data[j][1]) - float(list_data[j - 1][1])
        if change < greatest:
            greatest = change
            index = j
    
    return index

decrIndex = getGreatestDecr(data)
# print(decrIndex)
# print(data[decrIndex])

# This function will output the results to a text file
def writeTextFile(output):

    # First need to append newline character \n to the end of each row
    # Can use a new list to accomplish this
    outputFix = []
    for row in output:
        outputFix.append(row + '\n')

    # Specify path to write text file
    output_path = os.path.join('financial_analysis.txt')

    # Can use 'file = open(path, mode)' to write to the text file
    file = open(output_path, 'w')

    for row in outputFix:
        file.write(row)
    
    file.close()

# Write a function to output the data
def financialAnalysis(list_data, totalMonths, netTotal, average, incrIndex, decrIndex):
    li = list_data
    months = totalMonths
    total = netTotal
    avg = average
    iIndex = incrIndex
    dIndex = decrIndex

    # Make variables to store the greatest increase in profits and greatest decrease in profits
    # These values will be determined by li[index] - li[index - 1]
    profitIncrease = int(li[iIndex][1]) - int(li[iIndex - 1][1])
    profitDecrease = int(li[dIndex][1]) - int(li[dIndex - 1][1])

    # Make a list that will have each element be a line of output
    # This will be used for exporting a text file with the results
    output = []

    print('Financial Analysis')
    print('----------------------------')
    print(f'Total Months: {months}')
    print(f'Total: ${total}')
    print(f'Average Change: ${round(avg, 2)}')
    print(f'Greatest Increase in Profits: {li[iIndex][0]} (${profitIncrease})')
    print(f'Greatest Decrease in Profits: {li[dIndex][0]} (${profitDecrease})')

    output.append('Financial Analysis')
    output.append('----------------------------')
    output.append(f'Total Months: {months}')
    output.append(f'Total: ${total}')
    output.append(f'Average Change: ${round(avg, 2)}')
    output.append(f'Greatest Increase in Profits: {li[iIndex][0]} (${profitIncrease})')
    output.append(f'Greatest Decrease in Profits: {li[dIndex][0]} (${profitDecrease})')

    # Call function to export the text file
    writeTextFile(output)

# Call function above to display the financial analysis results
financialAnalysis(data, totalMonths, netTotal, average, incrIndex, decrIndex)
