def Sorting(arr): 
    arr.sort()   
    i = 0
    j = len(arr)-1
    while (i < j):  
        print(arr[j]) 
        j=j-1
        print(arr[i]) 
        i=i+1
    if (len(arr) % 2 != 0): 
        print(arr[i])  
   
arr = [1, 6, 9, 4, 3, 7, 8, 2]
Sorting(arr)
