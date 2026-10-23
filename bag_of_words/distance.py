"""A module for calculating the distance between two vectors"""

import numpy as np

def e_distance(matrix, q):
    """Euclidean distance from a binary vector q to every column of the matrix"""                   
    return np.linalg.norm(matrix - q, axis=0) 

def min_dis(dist, n):
    """Identifying the index of the minimum of an integer list excluding position n"""
    order = np.argsort(dist)
    # Exclude index n so that euclidean distance of a query with itself can be excluded
    order = order[order != n]
    return order[0]
