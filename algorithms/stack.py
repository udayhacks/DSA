#push pop peek size 



class Stack :
   
    
    def __init__(self) -> None:
        from collections import deque 
        self.s = deque([])
        self.length = 0 
        
    def push (self,data ):
        self.s.append(data)
        self.length+=1
    def pop (self) :
        self.s.pop()
        self.length-=1 
        
    def peek(self):
        if self.length == 0 :
            print( None)
        print( self.s[-1])
        
    def size(self):
        print(self.length ) 
    
    
    def print(self):
        for i in self.s :
            print(i)
    
    
    

    
a = Stack()

a.push(1)
a.print()
a.peek()
a.size()
a.push(22)
a.peek()
a.size()            
    
    



class node:
    def __init__(self,data = None) -> None:
        self.data = data 
        self.next = None
        
           
class stack_Linkedlist :
    def __init__(self) -> None:
        self.head = node()
        self.length = 0 
        
    def push (self,data) :
        self.length+=1
        k = node(data)
        k.next = self.head 
        self.head = k 
        
    def pop (self):
        self.length-=1 
        if self.head  :
            self.head = self.head.next
        else :
            print(None)
            
    def peek (self):
        print(self.head.data)
        
    def size(self):
        print(self.length)
        
        
    def print(self):
        curr = self.head 
        while curr :
            print(curr.data)
            curr = curr.next 
            
        
        
    
        
    
a = stack_Linkedlist()

a.push(1)
a.print()
a.peek()
a.size()
a.push(27)
a.peek()
a.size()            
    
    