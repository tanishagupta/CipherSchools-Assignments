def ParenthesisPrinting(string,add,opening,closing,number): 
    if closing == number: 
        for i in range(len(string)): 
            print(string[i], end = " ") 
        print() 
    else: 
        if(opening > closing): 
            string[add] = '}' 
            ParenthesisPrinting(string,add+1,opening,closing+1,number) 
        if(opening < number): 
            string[add] = '{' 
            ParenthesisPrinting(string,add+1,opening+1,closing,number) 
  
number = 4 
string = [""] * 2 * number
add=0
opening=0
closing=0
ParenthesisPrinting(string,add,opening,closing,number)
