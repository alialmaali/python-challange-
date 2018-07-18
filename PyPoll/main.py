#dependencies
import csv

file_to_load = "election_data.csv"
file_to_output = "election_analysis.txt"

#Total votes counter 
total_votes = 0

candidate_options = []
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0

#Read in the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.Dicreader(election_data)

    for row in reader:
        #Total vote count
        total_votes = total_votes + 1

        #extract the candidate name from each row
        candidate_name = row[2]

        # if the candidate does not match any existing candidate
        if candidate_name not in candidate_options:

            # Add it to the list of candidates in the running 
            candidate_options.append(candidate_options)


            #Begin Tracking that candidate voter count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count 
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# print and export 
with open (file_to_output, "w") as txt_File:
    # Print the findal vote count 
    election_results = (
        f"\n\nElection Results\n"
        f"----------------------\n"
        f"Total Votes: {total_votes}\n"
        f"----------------------\n"
    )
    print(election_results)
            
    # save the final vote count to the text file
    txt_File.wirte(election_results)

    # determine the winner by looping through the counnts
    for candidate in candidate_votes:
        # Retrieve the vote count and percentage 
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate 

         # print each candidate's voter count and percentage 
         voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
         print(voter_output)

        # save each candidate's voter count and percentage to text file
        txt_file.write(voter_output)

    #Print the winning candidate 
    winning_candidate_summary = (
         f"-----------------------------\n"
         f"Winner:{winning_candidate}\n"
         f"-----------------------------\n"
    )
    print(winning_candidate_summary)

#save the winning candidate's name to the text file 
txt_file.wirte(winning_candidate_summary)








