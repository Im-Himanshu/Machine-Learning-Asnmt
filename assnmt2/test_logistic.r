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



matrx3 = matrx2
matrx2 = matrx;
result = A%*%t(theta);
j = NROW(A);
answer = c(1:j);
i = 0;
result[,1] = result[,1]*1.6;
result[,2] = result[,2]*1.3;
result[,3] = result[,3]*1.9;
result[,4] = result[,4]*1;
result[,5] = result[,5]*1
result[,6] = result[,6]*1.8
result[,7] = result[,7]*3


for (i in 1:j){
  
  if(result[i,7] > 15){
    pmax =7
  }else{
    pmax = which.max( result[i,] )
  }
  answer[i] = pmax
}

#  which(A[i,] == max(result[i,]), arr.ind = TRUE)

write.table(answer, file.path(model_result), sep = ",", row.names = FALSE,col.names = FALSE,
            qmethod = "double",append = FALSE);

##########checking accuracy 
real  = "H:/R workspace/assnmt2/files1/public_solution2.txt";
input <- read.table(real,header = FALSE,sep = ",")
rAnswer <- t(t(as.matrix(input)));
u = NROW(rAnswer);
#answer[] = 1;
nr = NROW(theta);
Ccount = 1:nr;
matrx = matrix(1:(nr)^2,nr,nr)
matrx[,] = 0;
Ccount[] = 0#correct count
Acount = t(Ccount)
Ccount = Acount
Pcount = Acount
accuracy = Pcount
for(q in 1:u){
  Acount[rAnswer[q]] = Acount[rAnswer[q]]+1
  Pcount[answer[q]] = Pcount[answer[q]]+1
  matrx[rAnswer[q],answer[q]] = matrx[rAnswer[q],answer[q]]+1;
  if(rAnswer[q] == answer[q]){
    Ccount[answer[q]] = Ccount[answer[q]]+1
    }else{
    
  }
  
}
for(z in 1:NROW(theta)){
  accuracy[z] = Ccount[z]*100/Pcount[z];
}

#percentage = t(t(percentage))
accurate = sum(Ccount)
total = accurate*100/150000


value = 1:20 
value2 = (value)^2
value3 = (value)^3
value = cbind(value,value2,value3)

