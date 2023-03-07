


# " practice on the non -empty  single linked list "

class Node ():
    
    def __init__(self,data) :
        self.data = data
        self.next = None
        
    
class Single_linked_list():
    
    def __init__(self):
        self.head = None
        
     
    def front_join(self,data):
        n = Node(data)
        n.next = self.head
        self.head =n 
        
    def insert(self,prev,data): 
        n = Node(data)
        n.next = prev.next
        prev.next = n
      
    def append (self, data):
        n= Node(data)
        last = self.head 
        while last.next :
            last = last.next 
        last.next = n
        
    def Reverse(self):
        prev = None
        current= self.head
        while current:
            next_address = current.next 
            current.next = prev
            prev = current
            current = next_address 
            
        self.head = prev
        
        
        
        
    def Delete (self,position):
        
        current = self.head
        index = 0 
        
        while current.next and index < position :
            prev = current
            current = current.next
            index +=1
            
        if index ==0 :
            self.head = self.head.next
            
        elif  index < position :
            print(" position is beyond the limit ")
            
        else:
            print( ".--->> \"%s\" is the deleted item....."%current.data)
            #print("{}".format(current.data))
            prev.next = current.next
           

        
        
         
        
        
        
        
        
        
        
        
          
    def check(self,data) :
        key = self.head 
        count = 0 
        while key.next:
            count+=1
            if key.data == data :
                return print("FOUND AT" , count)
            key = key.next
        return print("NOT FOUND")
            
       
    def Print(self):
        node = self.head  # "node" isis the Node object 
        while node:
            print(node.data)  #print(node.next)                 
            node = node.next       
        print("*****************************************************")    
                 
print("Single_linked_list ..............")




first = Single_linked_list()
first.head = Node("first")


#first is the object of  singlelinked list object 
# first.head is 
# first.head.next  is none 


second = Node("second")
first.head.next = second 


third = Node("third")
second.next = third

four = Node("inserted11111")
third.next = four

first.Print()

first.insert(second, "inserted")

print("printed after inserted ")
first.Print()




first.append("fourth")
first.append("fifth")
first.front_join("zero")
first.Print()

first.check("fourth")
first.Reverse()
print("after reversing the data ")
first.Print()

print("DELETION AT A GIVEN POINT")

first.Delete(0)
first.Print()





