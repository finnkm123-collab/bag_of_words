"""A module for obtaining the file pths and reading files"""

import os

def get_path(file_name):
    """Obtain the path of the file you wish to implement bag of words on"""
    file_dir = os.path.dirname(__file__)    
    # Obtain relative path so .txt files can be located from the demo directory                    
    file_path = os.path.join(file_dir, "..", "data", file_name) 
    return file_path 

def get_paths2():
    """Obtain the paths of all .txt files in data/"""
    data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    paths = []
     # Sort so files load in a consistent order as the demo will use the fact that the query is sorted last
    for file in sorted(os.listdir(data_dir)): 
        if file.endswith(".txt"):                        
            paths.append(os.path.join(data_dir, file))   
    return paths                                         

def get_paths(data_dir):
    """Return sorted paths of all text files in data_dir"""
    paths = []
    # Sort so files load in a consistent order
    for file in sorted(os.listdir(data_dir)):          
        if file.endswith(".txt"): 
            paths.append(os.path.join(data_dir, file)) 
    return paths 























