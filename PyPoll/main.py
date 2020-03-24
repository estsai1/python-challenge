import os
import csv

#  election_data.csv is composed of three columns, 'Voter ID', 'County', and 'Candidate'
# Create a script that analyzes the votes and calculates the following:
    # Total number of votes cast
    # Complete list of candidates who received votes
    # % of votes each candidate won
    # Total number of votes each candidate won
    # Winner of the election based on the popular vote
# Print the analysis to the terminal and export a tile file with the results

# Specify path of the election_data.csv file
# Will use absolute path for now, change it to relative path at the end
election_data_csv = 'C:\\Users\\tenko\\Documents\\GitHub\\python-challenge\\PyPoll\\Resources\dummy.csv'
# election_data_csv = os.path.join('Resources', 'election_data.csv')

# Make a list to collect results
results = []
# results2 is a temporary list that will be used to clean up results
results2 = []

# Variables we'll need are total votes, winner
votes = 0
winner = ""

# Read in the csv file
with open(election_data_csv) as csvfile:

    # Split data on commas
    csvreader = csv.reader(csvfile, delimiter = ',')

    # Skip header
    next(csvfile)

    # Use for loop to add the data from the csv file to results
    for row in csvreader:
        results.append(row)

# This loop will create a new results list that omits county data
for row in results:
    # Check if duplicate voter IDs exist
    if row[0] not in results2:
        # If not, add them to the new list
        results2.append([row[0], row[2]])

# And now we can reassign this back to results
results = results2

# Write a method that will calculate and return total votes
def getTotalVotes(list):
    return len(list)

print(getTotalVotes(results))