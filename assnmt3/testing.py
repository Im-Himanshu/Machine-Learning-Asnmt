import math
import re
import codecs
import time
import scipy.sparse as sp
import  numpy as np
import  warnings
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
# dir = "himanshu"
# dir = dir.rstrip("\ ")
# dir = dir.lstrip('G')
# print(dir)
# row_ind = [0,0,1,1,2,2,3,3,1,0]
# np.array([1])/0   #'print' mode
# a = 5
#
#
# with warnings.catch_warnings():
#     warnings.filterwarnings('error')
#     try:
#         answer = 1 / 0
#     except Warning as e:
#         print('error found:', e)
# with np.errstate(divide='raise'):
#     try:
#         a / 0   # this gets caught and handled as an exception
#     except FloatingPointError:
#         print('oh no!')
#
# try:
#     np.array([1]) / 0
# except Warning:
#     print('Warning was raised as an exception!')
row_ind = [0,0,1,1,2,2,3,3,1,0,8,3]
row_ind2 = [0,1,2,3,11,11,4,5,10,6,7,8,9]
row_ind.sort(reverse=True)
print(row_ind)
k = 5
r2 = np.argpartition(row_ind2, -1 * k)
r = np.argpartition(row_ind2, -1 * k)[:1 * k]
r3 = np.argpartition(row_ind2, -1 * k)[-1 * k:]
print(r2)
print(r)
print(r3)


dict = {}
i = math.floor(.2)
i = .2
dict.update({i:3})
i = math.floor(.3)
dict.update({i:5})
i = math.floor(.1)
dict.update({i:1})
i = math.floor(.6)
dict.update({i:6})

for lol in dict :
    print(lol)
    print(dict.get(.2))

# ary = np.array[1,2,3]
# print(ary)
# ary.
# print(a)
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
