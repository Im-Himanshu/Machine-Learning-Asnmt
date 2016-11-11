import numpy as np
import pickle
import sys
#start_time = time.time()
# cmdinput = sys.argv[1:]
# doc_in  = cmdinput[0];
# doc_out = cmdinput[1];
doc_in = "Public test data/train.txt"
doc_out = "docout.txt"
lexicon = {}
titles = []  # will store the title exactly
titlecount = [] # will store the count correspoding to that title
# "imanshu", "goyal", "yahoo", "baby"
i =1
imfile = open(doc_in, 'r')
for line in imfile : #this will take the line by line
    words = line.split(" ");
    #performing availaiblity test on the title of the doc
    try :
       midwaste = titles.index(words[0]) # this will be order n
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
        # row_index.append(index)
        # this is not equal to null
        i2 = lexicon.get(word) # will return the index of the word that will be the key
        if i2 : #if i2 is not null then this
           column = i2
        else:
           lexicon.update({word:lexicon.__len__()})
        # col_index.append(column)
        # freq.append(1.0)   # if there are two element at same index then they will add up in sparsing


answer = np.zeros(shape=(titlecount.__len__(), lexicon.__len__()));
answer2 = np.zeros(shape=(titlecount.__len__(), lexicon.__len__()));
imfile = open(doc_in, 'r')
for line in imfile :
    words = line.split(" ")
    rowindex = titles.index(words[0])
    repeating = {}
    for word in words[1:] :
        check = repeating.get(word)
        columnindex = lexicon.get(word)
        answer2[rowindex, columnindex] += 1  # increase the frequency of that word doing simple one

        if check :
            repeating.update({word : 1} )
        else : # if the word was not in the local dictionary
          repeating.update({word : 1})
          answer[rowindex,columnindex]+= 1 #increase the frequency of that word doing simple one

allcount = answer;
allcount2 = answer2
No_of_doc  = titles.__len__() #change this if index is save absolutely
No_of_column = lexicon.__len__()
#print("--- after making tfidf %s seconds ---" % (time.time() - start_time))
#tfidf = sc.csc_matrix((freq,(row_index, col_index)),shape = (No_of_doc,No_of_column))
#allcount= tfidf.todense();
#allcount = answer;
allcount = np.array(allcount,order=[])
allcount = allcount+1; # doign laplase smothing
allcount2 = np.array(allcount2,order=[])
allcount2 = allcount2+1; # doign laplase smothing

titlecount = np.array(titlecount)
titlecount = titlecount+1;
# wordcount = []
# wordcount = [counts.sum() for counts in allcount]
probabilty = [];
i = 0
for pr in allcount :
    probabilty.append(pr*10000/titlecount[i]+1) # as the number is quite low so just eliminating initial zero
    i+=1
probabilty2 = [];
i = 0
for pr in allcount2 :
    probabilty2.append(pr*10000/titlecount[i]+1) # as the number is quite low so just eliminating initial zero
    i+=1

sum = titlecount.sum(); # will give the numerator of class probability
titleprob = titlecount/sum; # it will be probabilty

with open(doc_out, "wb") as myFile:
    pickle.dump(probabilty, myFile)
    pickle.dump(lexicon, myFile)
    pickle.dump(titles, myFile)
    pickle.dump(titleprob, myFile)
    pickle.dump(probabilty2, myFile)

#print("--- after making sparse %s seconds ---" % (time.time() - start_time))
