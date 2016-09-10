#!/usr/bin/env Rscript
# your code must have this first line.

# Test code for logistic regression part goes here

args <- commandArgs(trailingOnly = TRUE)

file_name <- args[1]
modeltheta <- args[2]
model_result <- args[3]

file_name  = "H:/R workspace/assnmt2/files1/public_test2.csv";
modeltheta = "sol2.txt";
model_result  = "testanswer2.txt";
input <- read.table(file_name,header = FALSE,sep = ",")
A <- t(t(as.matrix(input)));
result <- read.table(modeltheta,header = FALSE,sep = ",")
theta <- as.matrix(result);
result = A%*%t(theta);
j = NROW(A);
answer = c(1:j);
i = 0;
for (i in 1:j){
  pmax = which.max( result[i,] )
  answer[i] = pmax
}

#  which(A[i,] == max(result[i,]), arr.ind = TRUE)

write.table(answer, file.path(model_result), sep = ",", row.names = FALSE,col.names = FALSE,
            qmethod = "double",append = FALSE);