arr=[4,5,25,1]

for i in range(len(arr)):
    a=-1
    for j in range(i+1,len(arr)):
        if arr[j]>arr[i]:
            a=arr[j]
            break
    print(a)
