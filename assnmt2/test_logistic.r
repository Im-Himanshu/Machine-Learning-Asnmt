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
netdata2 = rbind("Co-effic1","Co-effic2","Co-effic3","Co-effic4","Co-effic5","Co-effic6","Co-effic7",
            "CCount1","CCount2","CCount3","CCount4","CCount5","CCount6","CCount7",
             "ACount1","ACount2","ACount3","ACount4","ACount5","ACount6","ACount7",
             "PCount1","PCount2","PCount3","PCount4","PCount5","PCount6","PCount7",
             "accuracy1","accuracy2","accuracy3","accuracy4","accuracy5","accuracy6","accuracy7",
             "netaccuracy%" , "Numberofcorrect"
             )









netdata = netdata2;

coeff = t(matrix(c(1.6, 1.2, 1.6, 1 , 1 , 1.6, 1,
                   1.8, 1.2, 1  , 1 , 1 , 1  , 1,
                   1.2, 1.8, 1  , 1 , 1 , 1  ,1,
                   1.5, 1.2, 1.6, 1 , 1 , 1  ,1,
                   1.5, 1.2, 1.6, 1 , 1 , 1.7,1
                   ),7,5))
for(x in 1:NROW(coeff)){

i = 0;
result[,1] = result[,1]*coeff[x,1];
result[,2] = result[,2]*coeff[x,2];
result[,3] = result[,3]*coeff[x,3];
result[,4] = result[,4]*coeff[x,4];
result[,5] = result[,5]*coeff[x,5]
result[,6] = result[,6]*coeff[x,6]
result[,7] = result[,7]*coeff[x,7];


for (i in 1:j){
  pmax = which.max( result[i,] )
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
Ccount = 1:NROW(theta);
Ccount[] = 0#correct count
Acount = t(Ccount)
Ccount = Acount
Pcount = Acount
accuracy = Pcount
for(q in 1:u){
  Acount[rAnswer[q]] = Acount[rAnswer[q]]+1
  Pcount[answer[q]] = Pcount[answer[q]]+1
  
  if(rAnswer[q] == answer[q]){
    Ccount[answer[q]] = Ccount[answer[q]]+1
  }
}
for(z in 1:NROW(theta)){
  accuracy[z] = Ccount[z]*100/Acount[z];
}

#percentage = t(t(percentage))
accurate = sum(Ccount)
total = accurate*100/150000

data = matrix(1:1,1,1)
coefficent = t(coeff[x,])
data = rbind(t(coefficent),t(Ccount),t(Acount),t(Pcount),t(accuracy),total,accurate)
netdata = cbind(netdata,data)
}

