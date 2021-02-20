def DuplicateOrNot(s):   
    l = []   
    for i in s:   
        if i == ')':  
            top = l.pop()    
            numinside = 0
            while top != '(':  
                numinside += 1
                top = l.pop()  
            if numinside < 1:  
                return False
        else: 
            l.append(i)  
    return True
  
 
string = "((a+b)+((c+d)))"
  
if DuplicateOrNot(string) == True:  
    print("No duplicates")  
else: 
    print("There is/are duplicate(s)") 
