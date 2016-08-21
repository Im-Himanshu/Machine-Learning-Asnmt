
#sometimes giving out of bound exception
test <- read.csv("F:/7th semester/COL341 Rahul garg/input/input.csv", header=FALSE)
mat <- as.matrix(test)
#mat =  matrix(c(5, 10,5, 8, 16, 7,9,18,2,4,8,7), nrow=3, ncol=4)
dimns1 = dim(mat)
y = mat[,dimns1[2]]  #for the ax=b equation

mat = mat[,-dimns1[2]]
mat = mat[-501,];
y = y [-501];
#y = t(y);
#mat = t(mat);  #transpose to make coumn vector as row
dimns = dim(mat)  
lead = 1;
thres = .0000001;
rowCount = dimns[1]
colCount = dimns[2]
i = 1 #edit this
quit = FALSE
row =1;
m = mat
while(row <= rowCount && !quit)
{
  
  #print(m);
  #println();
  
  #+1 because we have to process last one as well 
  if(colCount+1<= lead)
  {
    quit = TRUE
    break
  }
  
  i=row
  
  #finding the row with element at lead position is non zero to transfer it up.
  while(! quit && (m[i,lead] < thres) && (m[i,lead] > -1*thres) )
  {
    # this is just for resetting the row when starting to search in next column for leading non-zero
    #element
    #this will increase the row number if zero
    #below only if it is the last row than increase the column not row 
    if(rowCount < i+1)
    {
      #resetting the row to start over this time for new lead
      i=row;
      lead = lead+1;
      
      if(colCount+1 <= lead)
      {
        quit = TRUE;
        break;
      }
    }
    else {
      i = i+1;
    }
  }
  
  if(!quit)
  {
    #swaping
    temp = m[i,];
    tempy = y[i];
  
    m[i,] = m[row,]
    m[row,] = temp
    
    y[i] = y[row];
    y[row] = tempy;
    #swapRows(m, i, row);
    
    if(!((m[row,lead] < thres) && (m[row,lead] > -1*thres)) )
    {
      divider = m[row,lead];
      m[row,] = m[row,]/divider;
      y[row] = y[row]/divider;
      
    }  #  multiplyRow(m, row, 1.0f / m[row][lead]);
    i = 1
    while( i <= rowCount)
    {
      if(i != row)
        
      {  
        subtract = m[i,lead];
        m[i,] = m[i,] - subtract*m[row,]
         y[i] = y[i] - subtract*y[row];
      }#subtractRows(m, m[i][lead], row, i);
      i = i+1
    }
  }
  row = row+1;
}
count =0;
final = m[rowSums(m^2)>0,]
lol = dim(final);
lol[1] = lol[1]+1;
null = final[,lol[1]:lol[2]]; #to ignore the null rows
max = dim(null);
y = t(y)
demo2 = y;
for(lv in 2:max[2]){
  demo2 = rbind(demo2,y);
}


null = t(null)

solly = null-demo2;
null = -1*null;

crntdim = dim(null);
temp = lol[2]-lol[1]+1;#strength of the null space of a 
tempmat = diag(temp);
solly2 = cbind(solly,tempmat);
null2 = cbind(null,tempmat)
#null2 = t(null2)
final2 = t(final)
