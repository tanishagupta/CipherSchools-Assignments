def finding(arr,n,x):
    if n==0:
        return -1
    for i in range(n):
        for j in range(n):
            if arr[i][j]==x:
                print(i,j)


arr = [[ 10, 20, 30, 40 ],
       [ 15, 25, 35, 45 ],
       [ 27, 29, 37, 48 ],
       [ 32, 33, 39, 50 ]]
  
finding(arr,4,29)
