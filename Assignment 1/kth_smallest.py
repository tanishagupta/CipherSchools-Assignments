def kth(arr,n,k):
    arr.sort()
    for i in range(n):
        if arr[i]==arr[k-1]:
            return arr[i]
        else:
            continue

arr = [7, 10, 4, 3, 20, 15]
n = len(arr)
k = 4
print(kth(arr,n,k))
