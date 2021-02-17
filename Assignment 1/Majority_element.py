def Majority(arr, n):
 
    maxx = 0
    i = -1  
    for x in range(n):
        count = 0
        for y in range(n):
            if(arr[x] == arr[y]):
                count += 1
 
        if(count > maxx):
            maxx = count
            i=x
 
    if (maxx > n//2):
        print(arr[i])
    else:
        print("Majority element missing")

 
arr = [1, 1, 2, 1, 3, 5, 1]
n = len(arr)
Majority(arr, n)
