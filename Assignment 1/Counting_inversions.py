def InversionCount(arr):
    count=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if (arr[i]>arr[j]):
                count+=1
 
    print("Total inversions are: ",count)
 
 
arr = [3, 1, 2]
InversionCount(arr)
