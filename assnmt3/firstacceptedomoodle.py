import sys
import math
import re
import codecs
import time
# import winsound
from scipy import sparse as sc
from scipy import spatial
from scipy.sparse.linalg import svds
import numpy as np
start_time = time.time()

cmdinput = sys.argv[1:]
print(cmdinput)
z = int(cmdinput[1]) #dimension of lower subspace
k = int (cmdinput[3])+1 #number of similiar type documnet or query to be returnned
inputdir = cmdinput[5]   #location of  training file 5000 files

# given a title of document answer the title of k similiar document in the above data base
# doc_in .. doc_out
doc_in = cmdinput[7] #contain one title per line correspondin to each k document is to be returned
doc_out = cmdinput[9] #write answer of doc query in this file each line k output

# given a word output k similiar word predicted from the model
# term_in term_out
term_in = cmdinput[11] # list of word one query(word) per line k similiar word to be returned
term_out= cmdinput[13] #each line k word answer of word query seprated by ';    '

# given set of words give the title of the document which can be relevant
# line of word seprated by space
query_in = cmdinput[15] #doc_in
query_out= cmdinput[17] # doc_out only title of doc to be returned

# inputdir = "Documents"
# z = 100
# k = 10
# doc_in = "Sample I_O/doc_in.txt"
# doc_out = "Sample I_O/doc_out.txt"
# term_in = "Sample I_O/term_in.txt"
# term_out = "Sample I_O/term_out.txt"
# query_in = "Sample I_O/query_in.txt"
# query_out = "Sample I_O/query_out.txt"
# print(z,k,inputdir,trainingfile,wordqueryinput,wordqueryoutput,documnetqueryinput,documnetqueryoutput)
pattern = re.compile(r'\W+');
col_index = []
row_index = []
lexicon = {}
freq = []
titles = []
No_of_file = 5000
def build_sparse():
# "himanshu", "goyal", "yahoo", "baby"
    i =1
    for i in range(1,No_of_file+1) :
        imfile = codecs.open(inputdir+"/%s.txt"%(i), 'r', encoding='latin-1')
        title = imfile.readline().lower().rstrip("\n")
        titles.append(title)  #index is the key because we  have query based on the index in this
        article = imfile.read()
        words = pattern.split(article)
        column = 0
        for word in words:
            row_index.append(i-1)
            # this is not equal to null
            i2 = lexicon.get(word) # will return the index of the word that will be the key
            if i2 : #if i2 is not null then this
               column = i2
            else:
               lexicon.update({word:lexicon.__len__()})
            col_index.append(column)
            freq.append(1.0)   # if there are two element at same index then they will add up in sparsing
        i = i+1

vocabulary = build_sparse()
No_of_column = lexicon.__len__()
print("--- after making tfidf %s seconds ---" % (time.time() - start_time))
tfidf = sc.csc_matrix((freq,(row_index, col_index)),shape = (No_of_file,No_of_column))
print("--- after making sparse %s seconds ---" % (time.time() - start_time))
u, s, vt = svds(tfidf, z, which = 'LM')
S = np.diag(s)
docsvds = u.dot(S) # m x z  where m is no of doc see its correctness dot product see hwther it is coorect
wordsvds =  (vt.transpose()).dot(S) #n x z  n = number of words dot product for doc
print("--- after svd %s seconds ---" % (time.time() - start_time))

# # 111111111111111111111111111111111111111111 do querry
# print(doc_in)
# print(doc_out)
imfile = codecs.open(doc_in, 'r', encoding='latin-1')
outfile = open(doc_out, 'w')
querytitles = imfile.read()
#print(querytitles)
# print(titles.__len__())
for title in querytitles.splitlines() :
    j = titles.index(title.lower()) # get index of this doc will give the doc number
    docvector = docsvds[j]
    cosinevalue = [1-spatial.distance.cosine(docsvd, docvector) for docsvd in docsvds]  # find k smallest in this because it is distance itself
    ind = np.argpartition(cosinevalue, -1*k)[-1*k:]  # with highest k element because distance.cosine give angle rathen than value
    #print(ind)
    for i in ind :
        outfile.write(titles[i].rstrip("\n") + ";   ")
    outfile.write("\n") # it start new line
outfile.close()
print("--- after 1st query %s seconds ---" % (time.time() - start_time))


#22222222222222222222222222222222222222 word query
imfile = codecs.open(term_in, 'r', encoding='latin-1')
outfile = open(term_out, 'w')
querywords = imfile.read()
for word in querywords.splitlines() :
    j = lexicon.get(word.lower())  # get index of this doc   will give the doc number
    wordvector =  wordsvds[j]
    cosinevalue = [1 - spatial.distance.cosine(wordsvd, docvector) for wordsvd in wordsvds]  # find k smallest in this because it is distance itself
    dict = {}

    ind = np.argpartition(cosinevalue, -1 * k)[-1 * k:]  # with highest k element because distance.cosine give angle rathen than value
    for i in ind :
        for keys,value in lexicon.items():
            if value == i :
                outfile.write(keys.rstrip("\n") + ";   ")

    outfile.write("\n")  # it start new line

outfile.close()

print("--- after 2nd query %s seconds ---" % (time.time() - start_time))
# 33333333333333333333333333333333333333333333
# it is list of word rather than one word and article has to be suggested
imfile = codecs.open(query_in, 'r', encoding='latin-1')
outfile = open(query_out, 'w')
querytitles = imfile.read()
for line in querytitles.splitlines() :
    words = pattern.split(line) #simple word no need to perform special split
    length = words.__len__()
    answers = []
    for word in words:
        # this error won't occur but still in some cases it occur then do this
        j = lexicon.get(word)
        if j :
            j = j
        else :
            j =0
        answers.append(wordsvds[j])
    queryvector = np.sum([answer for answer in answers],axis = 0)
    queryvector = queryvector/length # average value of svds
    cosinevalue = [1-spatial.distance.cosine(docsvd, queryvector) for docsvd in docsvds]  # find k smallest in this because it is distance itself
    ind = np.argpartition(cosinevalue, -1*k)[-1*k:]  # with highest k element because distance.cosine give angle rathen than value
    outtitles = [outfile.write(titles[i].rstrip("\n") + ";   " )for i in ind ]
    outfile.write("\n") # it start new line
outfile.close()
print("--- %s seconds ---" % (time.time() - start_time))
# winsound.Beep(300,500)

