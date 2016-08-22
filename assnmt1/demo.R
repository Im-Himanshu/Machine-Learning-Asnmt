write(x, file = "data",
      ncolumns = if(is.character(x)) 1 else 5,
      append = FALSE, sep = " ")

write.table(mat, file.path( "H:/R workspace/test2.txt"), row.names = FALSE,col.
            append = FALSE,sep = ",")
write.table(mat, file.path("test2.txt"), sep = ",", row.names = FALSE,col.names = FALSE,
            qmethod = "double",append = FALSE)

file_name = "F:/Assignment1/testcases/input/testcase2/input.txt";
test <- read.table(file_name,header = FALSE,sep = ",")
mat <- as.matrix(test)
file_name1 = "F:/Assignment1/testcases/output/testcase2/out_1.txt";
test1 <- read.table(file_name,header = FALSE,sep = ",")
mat1 <- as.matrix(test)
file_name2 = "F:/Assignment1/testcases/output/testcase2/out_2.txt";
test1 <- read.table(file_name,header = FALSE,sep = ",")
mat2 <- as.matrix(test)
file_name3 = "F:/Assignment1/testcases/output/testcase2/out_3.txt";
test3 <- read.table(file_name,header = FALSE,sep = ",")
mat3 <- as.matrix(test)
