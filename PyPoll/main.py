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
election_data_csv = 'C:\\Users\\tenko\\Documents\\GitHub\\python-challenge\\PyPoll\\Resources\test_data.csv'
# election_data_csv = os.path.join('Resources', 'election_data.csv')

# Make a list to collect results
results = []

# Make a list to hold candidates, and another list to hold their votes
candidates = []
votes = []

# Variables we'll need are total votes, winner
totalVotes = 0
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

# This loop will fill the candidates list
for row in results:
    # Check if candidate name is also in the candidates list
    if row[2] not in candidates:
        # If not, add them to the list
        candidates.append(row[2])

# Now use a loop to fill votes list
# For each candidate in candidates...
for row in candidates:
    tempTotal = 0
    # Check each row in results[2] to see if it matches the candidate
    for row2 in results:
        if row2[2] == row:
            # If they match, increase vote counter for that candidate
            tempTotal = tempTotal + 1
    # Assign the candidate's vote count to votes list at the end of each iteration
    votes.append(tempTotal)

# There is now a list that holds all the election_data data, a list that holds all candidate names,
# and a list that holds votes that correspond to each candidate based on index number

# Write a method that will calculate and return total votes
def getTotalVotes(list):
    return len(list)

# Write method that will find the winner. This can be accomplished by finding the index value of
# the largest vote count in the votes list, then fetching the candidate name with the same index
# value in candidates. Return the candidate name
def findWinner(list_names, list_votes):
    names = list_names
    votes = list_votes
    
    largest = votes[0]
    index = 0

    for x in range(len(votes)):
        if votes[x] > largest:
            index = x
    
    win = names[index]

    return win

# Use methods to get the total votes and winner names
winner = findWinner(candidates, votes)
totalVotes = getTotalVotes(results)

# Write a method to print the results
# This will need 'candidates', 'votes', 'totalVotes', and 'winner'
def electionResults(candidates, votes, totalVotes, winner):
    print('Election Results')
    print('-------------------------')
    print(f'Total Votes: {totalVotes}')
    print('-------------------------')
    for index in range(len(candidates)):
        # Assign % of the vote to a temporary variable
        votePercent = (votes[index] * 100 / totalVotes)
        # Use :.3f formatting to force it to show 3 decimal places
        print(f'{candidates[index]}: {votePercent:.3f}% ({votes[index]})')
    print('-------------------------')
    print(f'Winner: {winner}')
    print('-------------------------')
    return

# Run the method that generates election results
electionResults(candidates, votes, totalVotes, winner)

# Write a method to export a text file with the results. Use PyBank for reference
def writeTextFile(candidates, votes, totalVotes, winner):

    # First specify a path for the output
    # Use absolute path for now, will fix to relative path at the end
    output_path = 'C:\\Users\\tenko\\Documents\\GitHub\\python-challenge\\PyPoll\\election_results.txt'
    # output_path = os.path.join('.', 'election_results.tx')

    # Make a list to hold output
    output = []

    # Build the output
    output.append('Election Results\n')
    output.append('-------------------------\n')
    output.append(f'Total Votes: {totalVotes}\n')
    output.append('-------------------------\n')
    for index in range(len(candidates)):
        votePercent = (votes[index] * 100 / totalVotes)
        output.append(f'{candidates[index]}: {votePercent:.3f}% ({votes[index]})\n')
    output.append('-------------------------\n')
    output.append(f'Winner: {winner}\n')
    output.append('-------------------------\n')

    # Use file thingy to write to the file
    file = open(output_path, 'w')

    for row in output:
        file.write(row)

    file.close()

# Run method to write results to a file
writeTextFile(candidates, votes, totalVotes, winner)

# For debugging
# print(totalVotes)
# print(candidates)
# print(votes)
# winner = findWinner(candidates, votes)
# print(winner)
