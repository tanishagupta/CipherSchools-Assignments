def func(arr,x):
    arr.sort()
    for i in range(len(arr)):
        if arr[i]==x:
            print(i)
            break
    for j in range(len(arr)-1,0,-1):
        if arr[j]==x:
            print(j)
            break

arr = [1, 3, 5, 5, 5, 5, 7, 123, 125]
x = 7
func(arr,x)
