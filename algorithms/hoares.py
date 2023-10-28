def hoares(arr,v) :
    
    
    #some error occured internally in the 
    
    n = len(arr)
    l = 0 
    h = n-1
    #arr[v], arr[l] = arr[l],arr[v]
    
    p = arr[5]
    
    i = l -1
    j = h -1
    
    while True :
        i = i +1
        while arr[i] <  p  :
            i+=1
        j = j+1
        while arr[j] >p :
            j-=1
        if i>= j :
            return j 
        arr[i],arr[j] = arr[j],arr[i]
        
    
    

arr= [10,80,30,90,50,70]
v = 2


hoares(arr, 4)
            
        
        
        