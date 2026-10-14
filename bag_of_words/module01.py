"""A module to implement a bag-of-words model that represents the relevance of a text file to a query"""

import numpy as np
import matplotlib.pyplot as plt
import os 

def get_path(file_name):
    """Obtain the path of the file you wish to implement bag of words on"""
    file_dir = os.path.dirname(__file__)
    file_path = os.path.join(file_dir, "..", "data", file_name)
    print(file_path)
    return file_path

def read_txt(file_path):
    """Read the file you wish to implement bag of words on"""
    with open(file_path) as f:
        txt = f.read()
        print(txt)

def txt_terms(file_path):
    """Clean the file you wish to implement bag of words on and transform into a list of the items"""
    with open(file_path, 'r') as f:
        txt = f.read()
        punctuation = [".", "'", ",", '"', ":", ";", "(", ")", "!", "?"]
        for p in punctuation:
            if p == "'":
                txt = txt.replace(p, "")
            else:
                txt = txt.replace(p, " ")
        maths_symbols = ["-", "+", "=", "/", "^", "*"]
        for m in maths_symbols:
            txt = txt.replace(m, f" {m} ")
        terms = txt.lower().split()
        print(terms)
        return terms

#path = get_path("pythagoras.txt")
#txt_terms(path)









