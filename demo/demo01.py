"""I will demonstrate the utility of this module by finding which document a query I have chosen is most similar to"""

import bag_of_words as bow
import os
import numpy as np

## In this case the query is a seperate document in the same directory as the text files

data_dir = os.path.join(os.path.dirname(__file__), "..", "data")  # Pull the path of the directory conatining text files
file_paths = bow.get_paths(data_dir)  # Create an ordered list of the file paths in this directory, including the query
print(file_paths)

V = bow.vocabulary(file_paths)  # Generate a list of the unique terms in all the documents + query
V = bow.vector(V)  # Vector with dimensions (n_terms, 1)

matrix = bow.ttd(V, file_paths)  # Stack the binary term-to-document (ttd) vector for each document in a matrix
q = matrix[:, [5]]  # seperate column 5 with query in, keeping the shape (m, 1)

d = bow.e_distance(matrix, q)  # Calculate the euclidean distance between each column of the ttd matrix and the query column, which is the column in the 5th position in this case
index_min = bow.min_dis(d, 5)  # Highllight the index of the distance minimising document excluding the query which has distance 0 with itself

print(file_paths[index_min])  # Document 2 has the smallest distance 

## Consider the case where the query is a seperate string 

data_dir = os.path.join(os.path.dirname(__file__), "..", "data") 
file_paths = bow.get_paths(data_dir) 
file_paths.pop(5)  # Removing the query from the path list

Q = bow.txt_terms("""Badminton is a racquet sport played using racquets to hit a shuttlecock across a net. Although it may be played with larger teams, the most common forms of the game are "singles" (with one player per side) and "doubles" (with two players per side). Badminton is often played as a casual outdoor activity in a yard or on a beach; professional games are played on a rectangular indoor court. Points are scored by striking the shuttlecock with the racquet and landing it within the other team's half of the court, within the set boundaries.""")
V = bow.unique_entries(bow.vocabulary(file_paths) + Q)  # Generate a list of all unoque terms in the documents plus the query
V = bow.vector(V) 

matrix = bow.ttd(V, file_paths)  # Generate seperate ttd matrix and vector
query = bow.binary_ttd_vector(V, Q) 

d = bow.e_distance(matrix, query)
order = np.argsort(d)
print(file_paths[order[0]])