
#sometimes giving out of bound exception
test <- read.csv("F:/7th semester/COL341 Rahul garg/input/input.csv", header=FALSE)
mat <- as.matrix(test)
#mat =  matrix(c(5, 5, 10, 8, 7, 16,9,2,18,4,7,8), nrow=3, ncol=4)
dimns1 = dim(mat)
y = mat[,dimns1[2]]  #for the ax=b equation
mat = mat[,-dimns1[2]]
mat = mat[-501,];
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
    i = i+1
    if(rowCount == i)
    {
      i=row;
      lead = lead+1;
      
      if(colCount+1 == lead)
      {
        quit = TRUE;
        break;
      }
    }
  }
  
  if(!quit)
  {
    #swaping
    temp = m[i,]
    m[i,] = m[row,]
    m[row,] = temp
    #swapRows(m, i, row);
    
    if(!((m[row,lead] < thres) && (m[row,lead] > -1*thres)) )
    {
      m[row,] = m[row,]/m[row,lead]
      
      
    }  #  multiplyRow(m, row, 1.0f / m[row][lead]);
    i = 1
    while( i <= rowCount)
    {
      if(i != row)
        
        m[i,] = m[i,] - m[i,lead]*m[row,]
      #subtractRows(m, m[i][lead], row, i);
    i = i+1
    }
  }
  row = row+1
}

count =0;
final = m[rowSums(m^2)>0,]
lol = dim(final);
lol[1] = lol[1]+1;
null = m[,lol[1]:lol[2]];
null = t(null)
null = -1*null;
crntdim = dim(null);

final2 = t(final)


