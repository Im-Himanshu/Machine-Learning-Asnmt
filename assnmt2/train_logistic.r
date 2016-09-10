#!/usr/bin/env Rscript
# your code must have this first line.

# Train code for logistic regression part goes here

args <- commandArgs(trailingOnly = TRUE)
example = 300; ##no of test data per example it should be equal for all
##assuming all of the cllasses have minimum of this much cases 

file_name <- args[1]
modeltheta <- args[2]
file_name  = "H:/R workspace/assnmt2/files1/input2.csv";
modeltheta = "sol2.txt";
input <- read.table(file_name,header = FALSE,sep = ",")
dimn = dim(input);
input = input[order(input$V55),]
mat <- as.matrix(input);
dimn = dim(mat)
m = dimn[1]
n = dimn[2]-1
y = mat[,n+1]
mat = mat[,-(n+1)]
x = t(t(mat));
##################create more feature here if want 
#for(j in 1:n){
 #}
#dimn = dim(x)
#m = dimn[1]
#n = dimn[2]
#-----------------------------------------------------#
max = y[m];
til = matrix(1:max*m,m,max)
til[,] = 0;
h = NROW(y)
for(p in 1:h){
  yi = y[p]
  til[p,yi] = 1;
}
#counting the total number of each class
counti = 1:max;
mid = 0;
for(w in 1:(max-1)){
  counti[w+1] = mid+sum(til[,w]);
  mid = counti[w+1];
}


#initializing theta
classes = max;
feature = n
#count occurnce 
theta = matrix(1:max*n,classes,feature)
##########################7 rows x   54 column
theta[,] = 0;
theta2 = theta;
example = 1;
alpha = .0000001;


#cases = t(t(c(1:example,counti[1]:(counti[1]+example),counti[2]:(counti[2]+example),
 #         counti[3]:(counti[3]+example),counti[4]:(counti[4]+example),
  #        counti[5]:(counti[5]+example))));
for(data in 1:example)
{##first example of all second example of all one by one not like
  ## all ones together and all twos together
  for(ds in 1:(classes-2)){
    example = (counti[ds]+data)
    
    denom = 0
    num= 0;
    seeme = 1:classes;
    for(c in 1:classes){
      seeme[c]  =t(theta[c,])%*%x[example,]
      denom = denom + 2.72^(seeme[c])
    }
    for(a in 1:classes){
      seeme2 = t(theta[a,])%*%x[example,];
      num = 2.72^(t(theta[a,])%*%x[example,])
      prob = num/denom
      for(b in 1:feature){
        #b=b+1;
        gradient = x[example,b]*(til[example,a]-prob)
        theta2[a,b] = theta[a,b] + alpha*gradient;
      }
    }
    theta3 = theta
    theta = theta2;
    example = example+1
    
    
    
  }
  
}

write.table(theta, file.path(modeltheta), sep = ",", row.names = FALSE,col.names = FALSE,
            qmethod = "double",append = FALSE);

