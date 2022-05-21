# Add our dependencies.

import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join('..',"Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.

    file_reader = csv.reader(election_data)

    #print header row. 
    headers = next(file_reader)
    print(headers)


#total number of votes cast


#complete list of candidates who received votes


#percentage of votes per candidate


#totalNumber of votes each candidate won


#winner of election based on popular vote