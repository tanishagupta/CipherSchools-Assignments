def func(l):
    l1 = []
    l2 = []
    for i in l:
        if i==0:
            l1.append(i)
        elif i==1:
            l2.append(i)
    j = l1+l2
    return j


l = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
print(func(l))
