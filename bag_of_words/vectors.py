"""A module for computing the binary term-to-document matrices"""

import numpy as np
from .text import unique_entries, load_terms

def vector(txt_list):
    """Transform a list of terms into a n x 1 vector, n being the number of entries in the list"""
    return np.array(txt_list).reshape(-1, 1)

def binary_ttd_vector(vocabulary_vector, doc_vector):
    """Create the binary term-to-document vector for a chosen query or document with respect to the vocabulary"""
    return np.isin(vocabulary_vector, doc_vector).astype(int) # Return 1s and 0s instead of boolean variables

def ttd(vocabulary_vector, file_paths):
    """Aggregate each doc's or query's binary term-to-document vector into a matrix"""
    columns = []
    for path in file_paths:
        doc_terms = unique_entries(load_terms(path))
        columns.append(binary_ttd_vector(vocabulary_vector, doc_terms))
    return np.column_stack(columns)