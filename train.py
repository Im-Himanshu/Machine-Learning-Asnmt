import codecs
import time
import numpy as np
import pickle
import sys
# import winsound
from scipy import sparse as sc
start_time = time.time()

cmdinput = sys.argv[1:]
doc_in  = cmdinput[1];
doc_out = cmdinput[2];


doc_in = "Public test data/train.txt"
doc_out_prob = "probability.txt"
doc_out_vocab = "vocab.txt"
doc_out_title = "titles.txt"
doc_out_count = "count.txt"
col_index = []
row_index = []
lexicon = {}
freq = []
titles = []
titlecount = []
def build_sparse():
# "himanshu", "goyal", "yahoo", "baby"
    i =1
    imfile = codecs.open(doc_in, 'r', encoding='latin-1')
    for line in imfile : #this will take the line by line
        words = line.split(" ");
        #performing availaiblity test on the title of the doc
        index = 0;
        try :
           midwaste = titles.index(words[0]) # this will be order n
           # midwaste = titles.get(words[0])  # will return the index of the word that will be the key
           # if midwaste is not null then this
           index = midwaste
           titlecount[index]+=1;
        except ValueError :
            # if i2 returened is null then this
            titles.append(words[0])
            # titles.update({words[0]: titles.__len__()+1})
            index = titles.__len__()-1  # because now the length is updated
            titlecount.append(1);

        column = 0
        for word in words[1:]: #Start index from 1 because 0th is the title which won't be there in testing
            row_index.append(index)
            # this is not equal to null
            i2 = lexicon.get(word) # will return the index of the word that will be the key
            if i2 : #if i2 is not null then this
               column = i2
            else:
               lexicon.update({word:lexicon.__len__()})
            col_index.append(column)
            freq.append(1.0)   # if there are two element at same index then they will add up in sparsing
vocabulary = build_sparse()

No_of_doc  = titles.__len__() #change this if index is save absolutely
No_of_column = lexicon.__len__()
print("--- after making tfidf %s seconds ---" % (time.time() - start_time))
tfidf = sc.csc_matrix((freq,(row_index, col_index)),shape = (No_of_doc,No_of_column))
allcount= tfidf.todense();
allcount = np.array(allcount,order=[])
allcount = allcount+1; # doign laplase smothing
wordcount = []
wordcount = [counts.sum() for counts in allcount]
probabilty = [];
i = 0
for pr in allcount :
    probabilty.append(pr*100/wordcount[i]) # as the number is quite low so just eliminating initial zero
    i+=1

with open(doc_out_prob, "wb") as myFile:
  pickle.dump(probabilty, myFile)

with open(doc_out_vocab, "wb") as myFile:
  pickle.dump(lexicon, myFile)

with open(doc_out_title, "wb") as myFile:
  pickle.dump(titles, myFile)

with open(doc_out_count, "wb") as myFile:
  pickle.dump(titlecount, myFile)

print("--- after making sparse %s seconds ---" % (time.time() - start_time))
