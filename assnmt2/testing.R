model_result22  = "files1/public_solution1.txt";
model_result2  = "testanswer.txt";

input3 <- read.table(model_result22,header = FALSE,sep = ",")
A2 <- t(t(as.matrix(input3)));
input4 <- read.table(model_result2,header = FALSE,sep = ",")
b2 <- t(t(as.matrix(input4)));
n = dim(A2);

error = (A2-b2)^2
total = sum(error)
total = total/n[1]
