def Rbinary_search(arr,f,l,n):
        if f>l :
            return -1
        
        mid = int((f +l) / 2) 
        if arr[mid]== n :
            return mid
        
         
        elif arr[mid] > n:
            return Rbinary_search(arr,f,mid-1,n)
        else:
            return Rbinary_search(arr,mid+1,l,n)
        
   
    
    
    
    
    
def Ibinary_search (arr,n):
    l= 0 
    u = len(arr)-1
    while(u-l>1) :
        mid = (l + u )//2
        if n > arr[mid] :
            l= mid
            
        else:
            u = mid          
            
    if arr[l] == n :
        return l 
    elif arr[u] == n :
        return u
     








def first_occuarence(arr, l , h , x) :
    if l> h :
        return -1 
    
    m = (l+h)//2

    if arr[m] == x :
        
        if m == 0 or arr[m-1] != arr[m] :
            return m
        
        return first_occuarence(arr, l , m-1,x) 
    

        
    elif arr[m] > x :
        return first_occuarence(arr,l,m-1,x)
    else :
        return first_occuarence(arr,m+1,h, x)
        

def last_occuarence(arr, l , h , x) :
    if l> h :
        return -1 
    
    m = (l+h)//2

    if arr[m] == x :
        
        if m == 0 or arr[m+1] != arr[m] :
            return m
        
        return last_occuarence(arr,m-1,h,x) 
    
    elif arr[m] > x :
        return last_occuarence(arr,l,m-1,x)
    else :
        return last_occuarence(arr,m+1,h, x)
        




def count_ocuarence(arr,l,h,x) :
    return last_occuarence(arr, l , h , x)  - first_occuarence(arr, l , h , x) + 1

              

    
    
a = [1,2,3,3,3,4,5,6,7,8,8,8,8,9,10]
# here directly it compares the mid values  in recursion
#print(Rbinary_search(a,0,len(a),3))
#print(binary_search(a,0,len(a),8))
#print(Ibinary_search(a,8))





print(first_occuarence(a , 0 , len(a)-1, 3))
print(last_occuarence(a , 0 , len(a)-1, 3))
print(count_ocuarence(a,0,len(a)-1,3))