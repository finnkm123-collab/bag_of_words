# bag_of_words

A Python package implementing a simple bag-of-words model for measuring how similar text documents are to one another, or to a query.

The package turns plain-text documents into binary term-to-document (TTD) vectors and compares them using Euclidean distance. Given a collection of .txt files and a query (either another file or a string), it identifies which document is most similar to the query. This has applications in information retrieval and machine learning.

## Installation

From inside the `bag_of_words` directory, install the package in editable mode:

```shell
python pip install -e .
```
The required dependencies are specified in `pyproject.toml` and will be installed automatically.

## How to use 

1. Locate files 

With an adjacent data/ directory containing .txt files you wish to measure, use get_paths2() to obtain a list of the paths of .txt files in data/ or get_path() (with a specific filename as the argument) to obtain the path of a specific .txt file.

If you run the package with a data directory in an alternative location, use get_paths(), with the full directory path as the argument, to obtain a list of the paths of all the .txt files in the directory.

2. Reading files, cleaning text, and building the vocabulary

To prepare the vocabulary of terms, the files of interest (including the query) must be cleaned, which means removing punctuation and padding certain symbols. Then terms seperated bhy whitespace can be translated into individual entries of
a list. The functions txt_terms() and load_terms() cover all of this, but take different arguments depending on the input type. load_terms() takes a file path, whilst txt_terms() takes a string. This makes txt_terms() useful for processing specific and tailored queries.

The output for both of the above must be reduced to only unique terms. unique_entries() takes this output and computes exactly that.

Reading and cleaning is streamlined in vocabulary(), which takes a list of file paths and returns a list of all the unique terms across the .txt files by internally calling txt_terms() and unique_entries().

3. Creating binary term-to-document (ttd) vectors and matrices

Each file or string becomes a binary vector the length of the vocabulary: position n is 1 if the nth vocabulary term appears in it, and 0 if not. 

vector() makes any list of strings into a 1D nd array, that has dimensions #terms x 1. This is important to make the following operations easier.

binary_ttd_vector() takes a vector of vocabulary terms and a vector of document specific terms, returning the binary ttd vector for that document.

ttd() extends this process to multiple documents at once by taking a list of file paths as one argument alongside a vector of vocabulary terms, and returning a matrix of binary ttd vectors.

4. Determining similarity 

Similarity is determined by the calculating the euclidian distance between binary ttd vectors. At a simple level, the smaller the euclidean distance of the vectors, the more similar the documents are.

e_distance() takes a binary matrix and vector as arguments and returns a list of the euclidean distances of each of the matrices columns with the binary vector.

min_dis() takes the above output as its argument and highlights the index of the column with the smallest euclidean distance excluding the distance in position n. This is important if the query term is in your ttd matrix, as I show in the demo. Then, the document associated with this column is the most similar to the query. 

## Demonstration

The complete demonstration can be run from the root directory using:

```sh
python demo/demo01.py
```