def CheckBalance(s): 
    l = [] 
    for i in s: 
        if i in ["(", "{", "["]: 
            l.append(i) 
        else:  
            if not l: 
                return False
            current_char = l.pop() 
            if current_char == '(': 
                if i != ")": 
                    return False
            if current_char == '{': 
                if i != "}": 
                    return False
            if current_char == '[': 
                if i != "]": 
                    return False
    if l=="": 
        return False
    return True
  
  

s = "[(])"
if CheckBalance(s): 
    print("It is Balanced") 
else: 
    print("It is Not Balanced")
