# Code to find k smallest elements
def kth(arr,k):
    arr.sort()
    for i in range(k):
        print(arr[i])

arr = [7, 10, 4, 3, 20, 15]
k = 4
kth(arr,k)




# Code to find kth smallest element
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



