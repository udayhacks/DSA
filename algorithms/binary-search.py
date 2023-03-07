def Rbinary_search(arr,f,l,n):
    if l>=f :
        mid = f +(l-f) // 2 
        if arr[mid]== n :
            return mid 
        elif arr[mid] > n:
            return Rbinary_search(arr,f,mid-1,n)
        else:
            return Rbinary_search(arr,mid+1,l,n)
        
    else:
        return -1 
    
    
    
    
    
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
     




            
def binary_search(  arr ,l,u,n):
    while(l<=u):
        mid = (l+u)//2
        if n == arr[mid] :
            return mid
        elif n > arr[mid]:
            l = mid+1
            
        else:
            u = mid-1
            
            
    return -1










              

    
    
a = [1,2,3,4,5,6,7,8,9,10]


print("Ologn,Ologn") 
# here directly it compares the mid values  in recursion
print(Rbinary_search(a,0,len(a),8))
print(binary_search(a,0,len(a),8))
print(Ibinary_search(a,8))