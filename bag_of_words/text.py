"""A module for cleaning text into lists of unique items"""

def txt_terms(txt):
    """Clean txt you wish to implement bag of words on and transform into a list of the items"""
    punctuation = [".", "'", ",", '"', ":", ";", "(", ")", "!", "?"] 
    # Remove punctuation making words that hold the same meaning recognisably the same 
    for p in punctuation:
        if p == "'":
            txt = txt.replace(p, "") 
        else:
            txt = txt.replace(p, " ") 
    maths_symbols = ["-", "+", "=", "/", "^", "*"] 
    # Pad maths symbols as they hold meaning that should be included
    for m in maths_symbols:
        txt = txt.replace(m, f" {m} ") 
    terms = txt.lower().split()  # Convert to lowercase so words with same meaning are recognised as the same  
    return terms

def load_terms(file_path):
    with open(file_path) as f:
        return txt_terms(f.read())

def unique_entries(terms):
    """Isolate the unique entries of a list, preserving order."""
    unique_terms = [] 
    for term in terms: 
        if term not in unique_terms:
            unique_terms.append(term) 
    return unique_terms

def vocabulary(file_paths):
    """Create a list of the unique items across all the docs in data/"""
    vocab = []
    for file in file_paths:
        vocab.append(load_terms(file))
    vocabulary = []
    for doc in vocab:
        for item in doc:
            vocabulary.append(item)
    return unique_entries(vocabulary)