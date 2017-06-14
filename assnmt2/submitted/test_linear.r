#!/usr/bin/env Rscript
# your code must have this first line.

# Test code for linear regression part goes here
args <- commandArgs(trailingOnly = TRUE)
#file_name  = "H:/R workspace/assnmt2/files1/public_test1.csv";
#modeltheta = "sol.txt";
#model_result  = "testanswer.txt";

file_name <- args[1]
modeltheta <- args[2]
model_result <- args[3]

input <- read.table(file_name,header = FALSE,sep = ",")
A <- as.matrix(input);
n = ncol(A)
for(j in 1:n){
  A = cbind(A,A[,j]*A[,j])
}
result <- read.table(modeltheta,header = FALSE,sep = " ")
theta <- as.matrix(result);

y = A%*%theta
write.table(y, file.path(model_result), sep = ",", row.names = FALSE,col.names = FALSE,
            qmethod = "double",append = FALSE);