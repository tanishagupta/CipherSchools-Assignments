l = [1, 2, 4, 5, 6]
    
def func(l):
    maxx = max(l)
    minn = min(l)
    for i in range(minn,maxx+1):
        if i not in l:
            print("Missing number is: ",i)
        else:
            continue

func(l)
