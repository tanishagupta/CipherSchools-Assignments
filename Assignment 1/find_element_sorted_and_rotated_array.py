arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
k = 3

def sortedandrotated(arr):
    for i in range(len(arr)):
        if arr[i]==k:
            print("Element ",k," is found at index ",i)
            break
        else:
            continue

sortedandrotated(arr)
