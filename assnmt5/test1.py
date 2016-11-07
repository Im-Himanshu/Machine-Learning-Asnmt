import codecs
import time
import sys
import numpy as np
import pickle
# import winsound
from scipy import sparse as sc
# cmdinput = sys.argv[1:]
# doc_in_test = cmdinput[1] #test file
# doc_in  = cmdinput[2]; #model file
# doc_out = cmdinput[3];  #result in this file

doc_in_test = "Public test data/test_att.txt"
doc_in  = "docout.txt"
doc_out = "answer.txt"
# notice in the tile field 1 is 0 and 2 is 1 and so on...
imfile = codecs.open(doc_in, "rb")
probabilties = np.array(pickle.load(imfile))
print("yahoo")
Vocablulary = pickle.load(imfile)
print("yahoo")

titles = pickle.load(imfile)
print("yahoo")
titlecount = np.array(pickle.load(imfile))

sum = titlecount.sum();
titlecount = titlecount/sum; # it will be probabilty
imfile = codecs.open(doc_in_test, 'r', encoding='latin-1')
outfile = open(doc_out, 'w')
for line in imfile:  # this will take the line by line
    words = line.split(" ");

    j = titles.__len__();
    totals = titlecount
    #    totals = np.array([1 for i in range(1,j)]); # have one for all
    for word in words:  # Start index from 1 because 0th is the title which won't be there in testing
        # this is not equal to null
        i2 = Vocablulary.get(word)  # will return the index of the word that will be the key
        if i2:  # if i2 is not null then this
            column = i2
            crnt = probabilties[:,column];
            totals = totals * crnt
    max = totals[0];
    indx =0
    i = 0
    for total in totals :
        if(total > max):
            indx = i;
            max = total;
        i+=1
    outfile.write(titles[indx])
    outfile.write("\n")
