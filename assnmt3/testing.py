import math
import re
import codecs
import time
import scipy.sparse as sp
import  numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import svds
#
# t = "himans%s"("goyal")
# t.__add__("goyal")
# print(t)
# imfile = codecs.open("Documents/1.txt", 'r', encoding='latin-1')
# querytitles = imfile.readline()
# print(querytitles);
# querytitles = imfile.read()
# for line in querytitles.splitlines() :
#     print(line)

#
#
# # a = "input1"
# # b= "input2"
# # c = a+"/"+b
# #
# # print(c)
# shape = (4,4)
# rows = 4
# column = 4
# z =2;
dir = "himanshu"
dir = dir.rstrip("\ ")
dir = dir.lstrip('G')
print(dir)
row_ind = [0,0,1,1,2,2,3,3,1,0]
ary = np.array[1,2,3]
print(ary)
ary.
print(a)
# col_ind = [0,1,2,3,0,1,1,0,2,0]
#
# lexicon = {}
# updater = {2:"yahoo"}
# lexicon.update(updater)
#
# print(lexicon.fromkeys("yahoo"))
# i =lexicon.get(2)
# if i :
#     print("me")
# else :
#     print ("me2")
# # for i in range(1,10) :
# #     mid = {"yahoo" : i}
# #     lexicon.update()
#
# print(lexicon)
# # answers = []
# # answers.append(row_ind)
# # answers.append(col_ind)
# #
# # x = np.sum([answer for answer in answers], axis=0)
# # print(x/2)
# # data =    [5.0,6.0,7.0,8.0,9.0,2.0,3.0,4.0,5.0,5.0]
# #
# # answer = sp.csc_matrix((data,(row_ind, col_ind)),shape = (rows,column))
# # # print(row_ind.__getitem__(8))
# # #answer.asfptype()
# # u, s, vt = svds(answer, z, which = 'LM')
# # print(u)
# # print(s)
# # print(vt)
