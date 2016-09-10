#!/usr/bin/env Rscript
# your code must have this first line.

# Train code for linear regression part goes here
args <- commandArgs(trailingOnly = TRUE)
file_name <- args[1]
outputfile <- args[2]
file_name  = "H:/R workspace/assnmt2/files1/input1.csv";
outputfile = "sol.txt";
test <- read.table(file_name,header = FALSE,sep = ",")
mat <- as.matrix(test);
dimn = dim(mat)
m = dimn[1]
n = dimn[2]-1
y = t(t(mat[,n+1]))
mat = mat[,-(n+1)]
x = t(t(mat));
for(j in 1:n){
  x = cbind(x,x[,j]*x[,j])
}

dimn = dim(x)
m = dimn[1]
n = dimn[2]
theta = t(t(c(1:n)))
theta[1:n,] = 0;
#theta2 = theta #renew theta 
#----------------------------------- calculating more inverse#
Xt = t(x)
p = Xt%*%x
i = det(p)
l = (Xt%*%y)
inv = solve(p)
moreinverse = inv%*%l
theta = moreinverse
#---------------------------------#
write.table(theta, file.path(outputfile), sep = ",", row.names = FALSE,col.names = FALSE,
            qmethod = "double",append = FALSE);








