def func(string,begg,last):
    curr = 0
    if(begg==last-1):
        print(string)
    else:
        for curr in range(begg,last):
            a=list(string)
            temp=a[begg]
            a[begg]=a[curr]
            a[curr]=temp

            func("".join(a),begg+1,last)
            
string = 'xyz'
n=len(string)
func(string,0,n)
