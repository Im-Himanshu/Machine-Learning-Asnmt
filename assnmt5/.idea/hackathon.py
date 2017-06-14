import fileinput
import numpy as np
ary = []
ary.append(1);
ary.sort();
ary.__len__()
ary.reverse()
ary.index(1) # will return the index of the 1 by iterating over array
# if want to use more advanced operation on array
ary = np.array(ary)
# now element wise operatio can be performed directly on it
ary +=1
dict = {}
dict.update({"yahoo" :1 })
dict.get("yahoo");
dict.__len__()
s = "1 String  me to a array"
splited = s.split(" ") # will split it
i = splited[0]
i = i+1 # this will work fine because python handle it



def process() :
    #do somethign here
    i = 5


    return i; # or can return anything
def main():
    #do something here
    i = 5


# if wnat to see more then see the third answer in this
# http://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == "__main__":
    # taking input in python
    for line in fileinput.input():
        print(line);

    main()
else :
    print("me")

#all the code is executed from first line and only skipped if thee is  a function def otherwise executed
# if class is cALLED from another then else will be executed in line order
# the above isthe python way of calling main so over and all above code will be executed




