import sys
import numpy as np
import pickle
import math
cmdinput = sys.argv[1:]
# doc_in_test = cmdinput[1] #test file
# doc_in  = cmdinput[2]; #model file
# doc_out = cmdinput[3];  #result in this file

doc_in_test = "Public test data/test_att.txt"
doc_in  = "docout.txt"
doc_out = "answer.txt"
# notice in the tile field 1 is 0 and 2 is 1 and so on...
imfile = open(doc_in, "rb")
probabilties = np.array(pickle.load(imfile))
print("yahoo")
Vocablulary = pickle.load(imfile)
print("yahoo")

titles = pickle.load(imfile)
print("yahoo")
titleprob = np.array(pickle.load(imfile))
print(titleprob)
probabilties = np.array(pickle.load(imfile)) # this will be probabilty2 varible form naive bayes
#sum = titlecount.sum(); # will give the numerator of class probability
#titlecount = titlecount/sum; # it will be probabilty
imfile = open(doc_in_test, 'r')
count = 0
outme = [];
for line in imfile:  # this will take the line by line
    count+=1;
    words = line.split(" ");
    j = titles.__len__();
    totals = np.log10(titleprob);  # remove 100 from the training for this
    for word in words:  # Start index from 1 because 0th is the title which won't be there in testing
        # this is not equal to null
        i2 = Vocablulary.get(word)  # will return the index of the word that will be the key
        #check = localdict.get(word);
        if i2:  # if i2 is not null then this
            column = i2
            crnt = probabilties[:,column];
            final = [];
            for single in crnt :
                if single <=1 :
                    final.append(single);
                else :
                    final.append(single*10000);
            final = np.array(final);
            totals = totals + np.log10(final)
    max = totals[0];
    indx =0
    i = 0
    for total in totals :
        if(total > max):
            indx = i;
            max = total;
        i+=1
    outme.append(titles[indx]+"\n");
outfile = open(doc_out, 'w')
s = "";
for i in range(0,outme.__len__()) :
    s += outme[i];
outfile.write(s)
#outfile.write("\n")
doc_in_test = "Public test data/test_labels.txt"
imfile1 = open(doc_in_test, 'r')
array1 = [];
imfile2 = open(doc_out, 'r')
array2 = [];
for line in imfile1:
    array1.append(line);

for line in imfile2:
    array2.append(line);
count = 0
total = array1.__len__();
for i in range(0,array2.__len__()):
    if array1[i] == array2[i] :
        count= count +1;


print(count*100/total)






