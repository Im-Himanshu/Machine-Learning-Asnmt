#examples taken from here: http://stackoverflow.com/a/1750187
import string #allows for format()
import math
import re
import codecs
from scipy import sparse as sc
import sys
from scipy.sparse import csc_matrix
from collections import Counter
import numpy as np


pattern = re.compile(r'\W+');
No_of_file = 2

# building the doc name array
mydoclist = [r for r in range(1,No_of_file+1)] #will be storing the name of the file
for i in range(0,No_of_file):
    mydoclist[i] = "Documents/%s.txt" % (i+1)
# print(mydoclist)
###################

def build_lexicon(corpus):
    lexicon = set()
    for doc in corpus:
        imfile = codecs.open(doc, 'r', encoding='latin-1')
        article = imfile.read().strip()
        words = pattern.split(article)
        lexicon.update([word for word in words])
    return lexicon


def freq(document):
    imfile = codecs.open(doc, 'r', encoding='latin-1')
    article = imfile.read().strip()
    words = pattern.split(article)
    tf_vector2 = [words.count(word) for word in vocabulary]
    return tf_vector2

vocabulary = build_lexicon(mydoclist)
#print(vocabulary)

# building tf-idf matrix in it
doc_term_matrix = []
freq_matrix = []
# print
# 'Our vocabulary vector is [' + ', '.join(list(vocabulary)) + ']'
for doc in mydoclist:
    # print
    # 'The doc is "' + doc + '"'
    ## returnvector with frequency of every word in the vocabulary
    tf_vector = freq(doc)
    tf_vector3 = [1 if x > 0 else 0.0 for x in tf_vector]
    # tf_vector_string = ', '.join(format(freq, 'd') for freq in tf_vector)
    # print ('The tf vector for Document %d is [%s]' % ((mydoclist.index(doc) + 1), tf_vector_string))
    doc_term_matrix.append(tf_vector)
    freq_matrix.append(tf_vector3)
    # here's a test: why did I wrap mydoclist.index(doc)+1 in parens?  it returns an int...
    # try it!  type(mydoclist.index(doc) + 1)
#
freq_matrix = np.transpose(np.array(freq_matrix))

doc_term_matrix = sc.csc_matrix(doc_term_matrix)


def l2_normalizer(vec):
    denom = np.sum([el**2 for el in vec])
    return [(el / math.sqrt(denom)) for el in vec]
doccount = [np.sum([el for el in tf_vector_mid]) for tf_vector_mid in freq_matrix]
my_idf_vector = doccount
# print 'Our vocabulary vector is [' + ', '.join(list(vocabulary)) + ']'
# print 'The inverse document frequency vector is [' + ', '.join(format(freq, 'f') for freq in my_idf_vector) + ']'

def build_idf_matrix(idf_vector):
    idf_mat = np.zeros((len(idf_vector), len(idf_vector)))
    np.fill_diagonal(idf_mat, idf_vector)
    return idf_mat

my_idf_matrix = build_idf_matrix(my_idf_vector)
# sparsing the matrix in the idf
my_idf_matrix = sc.csc_matrix(my_idf_matrix)
doc_term_matrix_tfidf = []

# # performing tf-idf matrix multiplication
for tf_vector in doc_term_matrix:
    doc_term_matrix_tfidf.append(np.dot(tf_vector, my_idf_matrix))
print(doc_term_matrix_tfidf)
doc_term_matrix_tfidf = np.multiply(doc_term_matrix,my_idf_vector)
print(doc_term_matrix_tfidf)
# print(my_idf_matrix)

# normalizing
doc_term_matrix_tfidf_l2 = []
for tf_vector in doc_term_matrix_tfidf:
    doc_term_matrix_tfidf_l2.append(l2_normalizer(tf_vector))

# print(vocabulary)
# print(np.matrix(doc_term_matrix_tfidf_l2))  # np.matrix() just to make it easier to look at


