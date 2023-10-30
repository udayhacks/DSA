def Sort(arr) :
    i = -1 
    n = len(arr)
    j = n-1
    
    while  True :
        
        i +=1
        while arr[i] < 0 :
            i+=1
        j -=1
        while arr[j] >0 :
            j-=1
        if i >=j :
            return 
        arr[i] ,arr[j] = arr[j] ,arr[i]
        
        
        
a = [-9,-4,3,-3,6]
Sort(a)
    
    
    