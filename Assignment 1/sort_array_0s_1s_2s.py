def func(arr):
    l1 = []
    l2 = []
    l3 = []
    for i in arr:
        if i==0:
            l1.append(i)
        elif i==1:
            l2.append(i)
        elif i==2:
            l3.append(i)

    d = l1+l2+l3
    return d

arr = [0,2,1,2,1,0,0,2,1]
print(func(arr))
