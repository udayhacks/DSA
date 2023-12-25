# used for detecting the cycle link  in the  linked list . 



def detect(head) :
    slow = fast =head   
    while fast != None and fast.next != None :
        slow = slow.next 
        fast = fast.next.next 
        if slow == fast :
            return fast
    if slow != fast :
        return head
        
    


def remove_cycle (head): 
    fast = detect(head) 
    slow = head   
    if slow == fast :
        return  
    while slow.next  != fast.next :
        slow = slow.next 
        fast = fast.next      
    fast.next = None 
    
    

def combined_func(head):
    slow = fast = head 
    while fast != None  and fast.next != None : 
        slow = slow.next 
        fast = fast.next.next 
        if slow == fast :
            break 
    if slow != fast :
        return 
    
    slow = head 
    while slow.next != fast.next :
        slow = slow.next 
        fast = fast.next 
        
    fast.next = None 
    
    
    
    
















    
class node:
    def __init__(self,data):
        self.data = data 
        self.next = None 
        
        
        
head = node(1)
a = node(2)
b = node(3)
c = node(4)
     
head.next = a
a.next = b 
b.next = c 
c.next = a 


#remo(head)
remove_cycle(head)
 
"""
remove_cycle(head)     
"""
curr = head
while curr :
    print(curr.data)
    curr = curr.next