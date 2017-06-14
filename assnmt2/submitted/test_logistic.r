#!/usr/bin/env Rscript
# your code must have this first line.

# Test code for logistic regression part goes here

args <- commandArgs(trailingOnly = TRUE)

file_name <- args[1]
modeltheta <- args[2]
model_result <- args[3]

#file_name  = "H:/R workspace/assnmt2/files1/public_test2.csv";
#modeltheta = "sol2.txt";
#model_result  = "testanswer2.txt";
input <- read.table(file_name,header = FALSE,sep = ",")
A <- t(t(as.matrix(input)));


result <- read.table(modeltheta,header = FALSE,sep = ",")
theta <- as.matrix(result);
result = A%*%t(theta);
j = NROW(A);
answer = c(1:j);
i = 0;
result[,1] = result[,1]*4.3;
result[,2] = result[,2]*5.1;
#result[,3] = result[,3]/8-.3;
#result[,4] = result[,4]-2.0;
#result[,6] = result[,6]
#result[,7] = result[,7] - .7;
for (i in 1:j){
  pmax = which.max( result[i,] )
  answer[i] = pmax
}
##average = t(t(average))

#  which(A[i,] == max(result[i,]), arr.ind = TRUE)

write.table(answer, file.path(model_result), sep = ",", row.names = FALSE,col.names = FALSE,
            qmethod = "double",append = FALSE);

##########checking accuracy 
#real  = "H:/R workspace/assnmt2/files1/public_solution2.txt";
#input <- read.table(real,header = FALSE,sep = ",")
#rAnswer <- t(t(as.matrix(input)));
#u = NROW(rAnswer);
#answer[] = 7;
#count = 0;

#for(q in 1:u){
 # if(rAnswer[q] == answer[q]){
 #   count = count+1
 # }
#}
#percentage = count*100/u

