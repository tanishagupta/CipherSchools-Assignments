def finding(arr,length,num):
    if length==0:
        return -1
    for i in range(length):
        for j in range(length):
            if arr[i][j]==num:
                print(i,j)


arr = [[ 10, 20, 30, 40 ],
       [ 15, 25, 35, 45 ],
       [ 27, 29, 37, 48 ],
       [ 32, 33, 39, 50 ]]
  
finding(arr,4,29)
