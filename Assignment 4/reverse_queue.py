## Wasn't able to understand at first but then took help and understood it

class Queue: 
    def __init__(self): 
        self.elements = [] 
    def isEmpty(self): 
        return self.elements == [] 
  
    def addition(self, item): 
        self.elements.append(item) 
  
    def pop(self): 
        return self.elements.pop(0) 
  
    def front(self): 
        return self.elements[0] 
  
    def printQueue(self): 
        for i in self.elements: 
            print(i, end =" ") 
        print("") 
  
   
def reverseQueue(q): 
    if (q.isEmpty()): 
        return 
    data = q.front(); 
    q.pop();   
    reverseQueue(q) 
    q.addition(data) 
  
  
# Driver Code 
q = Queue() 
q.addition(56) 
q.addition(27) 
q.addition(30) 
q.addition(45) 
q.addition(85) 
q.addition(92) 
q.addition(58) 
q.addition(80)  
reverseQueue(q) 
q.printQueue() 
