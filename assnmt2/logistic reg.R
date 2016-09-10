#Read data set
#data <- read.csv("H:/R workspace/assnmt2/input1.csv",header = FALSE,sep = ",")

file_name  = "H:/R workspace/assnmt2/files1/input1.csv";
file_name2  = "H:/R workspace/assnmt2/files1/public_test1.csv";
file_result  = "H:/R workspace/assnmt2/files1/public_solution1.txt";
input <- read.table(file_name,header = FALSE,sep = ",")
mat <- as.matrix(input);

test <- read.table(file_name2,header = FALSE,sep = ",")
testing <- as.matrix(test);

result <- read.table(file_result,header = FALSE,sep = " ")
testy <- as.matrix(result);
dimn = dim(mat)
m = dimn[1]
n = dimn[2]-1
y = t(t(mat[,n+1]))
mat = mat[,-(n+1)]
x = t(t(mat));
alpha = .001;
beta = .01;#for ridge regression
#code for feature expansion means create new feature.
#for(i in 1:n){
  for(j in 1:n){
   x = cbind(x,x[,j]*x[,j])
  }
#}
dimn = dim(x)
m = dimn[1]
n = dimn[2]
theta = t(t(c(1:n)))
theta[1:n,] = 0;
theta2 = theta #renew theta 
Xt = t(x)
p = Xt%*%x
i = det(p)
l = (Xt%*%y)
inv = solve(p)
moreinverse = inv%*%l

#Dependent variable
#y <- data$profit
##Independent variable
#x <- data$population
#Add ones to x 
#x <- cbind(1,x)
theta = moreinverse

#Calculate cost
cost <- sum(((testing%*%theta)- testy)^2)/(2*m)
# Set learning parameter
#Number of iterations
iterations <- 60
save = c(1:n);
save2 = c(1:n);
# updating thetas using gradient update
for(i in 1:iterations)
{
 # theta[1] <- th.eta[1] - alpha * (1/m) * sum(((x%*%theta)- y))
  #theta[2] <- theta[2] - alpha * (1/m) * sum(((x%*%theta)- y)*x[,2])
  
  for (i in 1:n){
    save2[i] = t(sum((y-(x%*%theta))*x[,i]));
    save[i] = alpha * (1/m) * sum((y-(x%*%theta))*x[,i]);
  #theta2[i] <- (1-2*alpha*beta)theta2[i] + 2*alpha * ((1/m) * sum((y-(x%*%theta))*x[,i])+ 2*beta*theta[i])
  theta2[i] <- (1-2*alpha*beta)*theta2[i] + 2*alpha * sum((y-(x%*%theta))*x[,i])
  }
  theta = theta2;
  cost <- sum(((x%*%theta)- y)^2)/(2*m)
  
}
cost <- sum(((x%*%theta)- y)^2)/(2*m)
#Predict for areas of the 35,000 and 70,000 people
predict1 <- c(1,3.5) %*% theta
predict2 <- c(1,7) %*% theta

demo = t(t(c(1:6)))
demo2 = t(t(c(1:6)))
demo3 = demo*demo2



