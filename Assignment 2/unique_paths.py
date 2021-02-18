def UniquePaths(m1,m2): 
    if(m1==1 or m2==1): 
        return 1
    return UniquePaths(m1-1,m2)+UniquePaths(m1,m2-1) 
  

m1 = 3
m2 = 7
print(UniquePaths(m1,m2)) 
