def PeakElement(arr):
    if (len(arr) == 1) :
        print(arr)
    if (arr[0] >= arr[1]) :
        print(arr[0])
    if (arr[len(arr)-1] >= arr[len(arr)-2]) :
        print(arr[len(arr)-1])
  
    for i in range(1,len(arr)-1) :
        if (arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]) :
            print(arr[i])
             
arr = [10, 20, 15, 2, 23, 90, 67]
PeakElement(arr)
