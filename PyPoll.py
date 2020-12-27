#The data we need to retrieve.
#1. The total number of votes cast in the election
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

#Add dependencies
import csv
import os

#Assign a variable to load a file from a path (using INDIRECT PATH)
file_to_load = os.path.join("Resources","election_results.csv")

#Assign a variable to save the file to a path (using INDIRECT PATH)
file_to_save = os.path.join("analysis","election_analysis.txt")

#Initialize a total vote counter
total_votes = 0
#Declare a new list
candidate_options = []
#Declare a dictionary #candidate_votes = {"candidate_name1": votes, "candidate_name2": votes, "candidate_name3": votes}
candidate_votes = {}
#Declare a variable that holds an empty string value for the winning candidate
winning_candidate = ""
#Declare a variable for the "winning count" equal to zero
winning_count = 0
#Declare a variable for the "winning percentage" equal to zero
winning_percentage = 0

#Open the election results
with open(file_to_load) as election_data:

    #To do: read and analyze the data here
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    #Read the header row
    headers = next(file_reader)
    #print(headers)
    
    #Print each row in the CSV file
    for row in file_reader:
        
        #Add to the total vote count
        total_votes += 1
        
        #print(row[0]) print the first item for each row
        #print(row)
        #Print the candidate name from each row
        candidate_name = row[2]

        #To get unique names, check if the candidate has already been added to the list
        if candidate_name not in candidate_options:
            #Add the candidate_name to the candidate_options list using the append() method
            candidate_options.append(candidate_name)

            #Count the votes for each candidate
            #Instantiate a candidate as a key for the dictionary and set the vote count to zero
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#print(f"candidate_options: {candidate_options}")
#print(f"candidate_votes: {candidate_votes}") #C=85213, D=272892, R=11606

#Save the results to a text file
with open(file_to_save, 'w') as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
    )
    print(election_results, end="") #By default, the "end" parameter will print a newline, \n. 

    #Save the final vote count to the text file
    txt_file.write(election_results)

    #Determine the percentage of votes for each candidate by looping through ...
    #Iterate through the candidate list
    for candidate_name in candidate_votes:
            #Retrieve vote count of a candidate
            votes = candidate_votes[candidate_name]
            #Calculate the percentage of votes
            vote_percentage = float(votes) / float(total_votes) * 100
            #Print the candidate name and percentage of votes
            #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)

            #Save the candidate results to the text file
            txt_file.write(candidate_results)

            #Determine if the vote count that was calculated is greater than the winning_count
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                #Set the winning_count equal to the votes and the winning_percentage equal to the vote_percentage
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name

    #print(f"The winning candidate is: {winning_candidate} with {winning_count:,} votes, which means {winning_percentage:.1f}% of the vote.")
    winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winner Vote Count: {winning_count:,}\n"
        f"Winner Percentage: {winning_percentage:.1f}\n"
        f"---------------------------\n"
    )
    print(winning_candidate_summary)
    #Save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)




