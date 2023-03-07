

"""
here array is rotated m time 

 cyclicly rotated
 
"""




def cylic_rotation(a, n ,m):
    
    for i in range(m):    
        x = a[n-1]
        for i in range(n-1, 0 , -1):
            a[i]= a[i-1]
            
        a[0]=x
        
    return a


a = [1,2,3,4,5,6]
n = len(a)
m =4
cylic_rotation(a,n,m)




print(*a)
    
