def PathCal(matrix1, matrix2): 
    if(matrix1==1 or matrix2==1): 
        return 1
    return PathCal(matrix1-1,matrix2)+PathCal(matrix1,matrix2-1) 
  
matrix1 = int(input())
matrix2 = int(input())
print(PathCal(matrix1,matrix2)) 
