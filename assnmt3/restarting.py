#examples taken from here: http://stackoverflow.com/a/1750187
import math
import re
import codecs
import time
import winsound
from scipy import sparse as sc
from scipy.sparse.linalg import svds
from scipy import spatial
import numpy as np
pattern = re.compile(r'\W+');
No_of_file = 20
start_time = time.time()
z = 19
k =10

# building the doc name array
mydoclist = [r for r in range(1,No_of_file+1)] #will be storing the name of the file
#
# import scipy.sparse as sp
# <sparse matrix> = sp.csc_matrix((data, (row_ind, col_ind)), [shape=(M, N)])

for i in range(0,No_of_file):
    mydoclist[i] = "Documents/%s.txt" % (i+1)

row_index = []
col_index = []
lexicon = []
freq = []
titles = []
def build_sparse(corpus):
# "himanshu", "goyal", "yahoo", "baby"
    i = 0
    for doc in corpus:
        imfile = codecs.open(doc, 'r', encoding='latin-1')
        titles.append(imfile.readline())
        article = imfile.read()
        words = pattern.split(article)
        #print(words)
        column = 0
        for word in words:
            row_index.append(i)
            try:
                column = lexicon.index(word.lower())
            except ValueError:
                column = lexicon.__len__()
                lexicon.append(word.lower())
            col_index.append(column)
            freq.append(1.0)
            #print(column)
        i = i+1


build_sparse(mydoclist)
No_of_column = lexicon.__len__()
print(No_of_column)
# no_of file = row
# and the lexicon is the dictionary made
answer = sc.csc_matrix((freq,(row_index, col_index)),shape = (No_of_file,No_of_column)).todense()
print("--- %s seconds ---" % (time.time() - start_time))

u, s, vt = svds(answer, z, which = 'LM')
S = np.diag(s)
# print(u)
# print(s)
# print(vt)
print(S.shape)

docsvd = u.dot(S) # m x z  where m is no of doc see its correctness dot product see hwther it is coorect
wordsvd =  (vt.transpose()).dot(S) #n x z  n = number of words dot product for doc
# print(docsvd)
# print(wordsvd)
print(wordsvd.shape)
#print(titles)
#111111111111111111111111111111111111111111 do querry
imfile = codecs.open("Sample I_O/doc_in.txt", 'r', encoding='latin-1')
outfile = open("doc_out.txt", 'w')
querytitles = imfile.read()
for title in querytitles.splitlines() :
    j = titles.index(title+"\n") # get index of this doc   will give the doc number
    docvector = docsvd[j]
    cosinevalue = [1-spatial.distance.cosine(docsvds, docvector) for docsvds in docsvd]  # find k smallest in this because it is distance itself
    ind = np.argpartition(cosinevalue, -1*k)[-1*k:]  # with highest k element because distance.cosine give angle rathen than value
    outtitles = [outfile.write(titles[i].rstrip("\n") + ";   " )for i in ind ]
    outfile.write("\n") # it start new line

outfile.close()

#22222222222222222222222222222222222222 word query
imfile = codecs.open("Sample I_O/term_in.txt", 'r', encoding='latin-1')
outfile = open("term_out.txt", 'w')
querywords = imfile.read()
for word in querywords.splitlines() :
    j = lexicon.index(word)
    print(j)
    wordvector =  wordsvd[j]
    cosinevalue = [1 - spatial.distance.cosine(wordsvds, docvector) for wordsvds in wordsvd]  # find k smallest in this because it is distance itself
    ind = np.argpartition(cosinevalue, -1 * k)[-1 * k:]  # with highest k element because distance.cosine give angle rathen than value
    print(ind)
    outwords = [outfile.write(lexicon[i].rstrip("\n") + ";   ") for i in ind]
    outfile.write("\n")  # it start new line

outfile.close()


    # report he top 8
    #dosomethign and get the index of the owrd

    # imwrite some thing in the file
# 33333333333333333333333333333333333333333333
# it is list of word rather than one word and article has to be suggested
imfile = codecs.open("Sample I_O/query_in.txt", 'r', encoding='latin-1')
outfile = open("query_out.txt", 'w')
querytitles = imfile.read()
for line in querytitles.splitlines() :
    # query_col_index = []
    # query_row_index = []
    # query_freq = []
    words = pattern.split(line) #simple word no need to perform special split
    length = words.__len__()
    answers = []
    for word in words:
        j = lexicon.index(word.lower())
        print(j)
        answers.append(wordsvd[j])
    queryvector = np.sum([answer for answer in answers],axis = 0)
    queryvector = queryvector/length # average value of svds
    cosinevalue = [1-spatial.distance.cosine(docsvds, queryvector) for docsvds in docsvd]  # find k smallest in this because it is distance itself
    ind = np.argpartition(cosinevalue, -1*k)[-1*k:]  # with highest k element because distance.cosine give angle rathen than value
    outtitles = [outfile.write(titles[i].rstrip("\n") + ";   " )for i in ind ]
    outfile.write("\n") # it start new line
outfile.close()

print("--- %s seconds ---" % (time.time() - start_time))













# winsound.Beep(300,500)

