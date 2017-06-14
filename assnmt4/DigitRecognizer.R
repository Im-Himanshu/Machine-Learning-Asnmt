# Creates a simple random forest benchmark
# this is the first program based on the randomforest library
# this idea is picked up from the discussion forum of kaggle 
# using the random forest library of the random forest
library(randomForest)
library(readr)

set.seed(0)

# read the file form the input folder

args <- commandArgs(trailingOnly = TRUE)
#trainingfile = args[1]
#testingfile = args[2]
trainingfile  = "input/train.csv"
testingfile = "input/test.csv";
inputtrain = read_csv(trainingfile)
inputtest  = read_csv(testingfile)

# how many train file
NoofTrain = 10000
# how many trees to make 
NoofTrees = 25

#extracting the pixel from the answer in the training data
Daata = sample(1:nrow(inputtrain), NoofTrain)
Answer = as.factor(inputtrain[Daata,]$label)
inputtrain = inputtrain[Daata,-1]
# this is from the library of the random forest
#this was used t oamke predictions this is internal based in decision tree in which it classify 
# data based on the entropy 
result = randomForest(inputtrain, Answer, xtest=inputtest, ntree=NoofTrees)


# this will make the prediction based on the above made random forest
predictions=data.frame(ImageId=1:nrow(inputtest),
                       Label=levels(Answer)[result$test$predicted])
# take the first column of above outout image
head(predictions)

#write the aboe file 
write_csv(predictions,"output.csv") 
