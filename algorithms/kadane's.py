l = [-4,-3,-2,3,1,-2,-3,6,-6,-4,2,1]

def kadanes(l):
    c= 0 
    m = l[0]
    s , e, p = 0,0,0
    for i in range(len(l)):
        c +=l[i]
        if c >m :
            s = p 
            e = i 
            m = c
            
        if c < 0 :
            c =0
            p = i+1
            
            
    return m



print(kadanes(l))
        
        
