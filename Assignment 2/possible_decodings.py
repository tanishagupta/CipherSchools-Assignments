# Wasn't able to understand the logic earlier but then took help and understood it.

def DecodingCount(num,n): 
    count = [0] * (n + 1)
    count[0] = 1
    count[1] = 1
    for i in range(2, n + 1): 
        count[i] = 0 
        if (num[i - 1] > '0'): 
            count[i] = count[i - 1]
        if (num[i - 2] == '1' or (num[i - 2] == '2' and num[i - 1] < '7')): 
            count[i] += count[i - 2]
 
    return count[n]
 

num = "896" 
n = len(num) 
print(DecodingCount(num,n))
