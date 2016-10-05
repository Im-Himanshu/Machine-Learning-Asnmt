#!/usr/bin/env Rscript
# your code must have this first line.

# Test code for linear regression part goes here
args <- commandArgs(trailingOnly = TRUE)

file_name <- args[1]
modeltheta <- args[2]
model_result <- args[3]

file_name  = "H:/R workspace/assnmt2/files1/public_test1.csv";
modeltheta = "sol.txt";
model_result  = "testanswer.txt";

input <- read.table(file_name,header = FALSE,sep = ",")
A <- t(t(as.matrix(input)));
r = dim(A)
r = ncol(A)
x0 = c(1:r);
x0 = 1;
for(i in 1:r){
  A = cbind(A,A[,i]*A[,i])
}
A = cbind(x0,A);

dimn = dim(A);
m = dimn[1]
n= dimn[2]
max = c(1:n)
min = c(1:n)
sum = c(1:n)
##normalizing
for(d in 1:n){
  max[d] = max(A[,d])
  min[d] = min(A[,d])
  sum[d] = sum(A[,d])
  }
average = sum/m

d= 1;
for(d in 1:n){
 # A[,d] = (A[,d])/(max[d]); 
}

result <- read.table(modeltheta,header = FALSE,sep = " ")
theta <- as.matrix(result);

y = A%*%theta
write.table(y, file.path(model_result), sep = ",", row.names = FALSE,col.names = FALSE,
            qmethod = "double",append = FALSE);