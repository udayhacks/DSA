from math import gcd 



def GCD (l):
   
    if len(l) == 1:
        return l[0]
    g = gcd(l[0],l[1])
    if len(l) == 2 :
        return g
    gcd(l[0],l[1])
    
    for i in range(1,l
                   
                   en(l)-1):
        g = gcd(g,l[i+1])
        if g == 1 :
            return g
        
    return g

print(GCD([15,81,78]),gcd(15,81,78))

