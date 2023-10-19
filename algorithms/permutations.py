def permutation(s,i):
    n = len(s)
    if i == n-1 :
        return s 
    for j in range(i , n ):
        s[i], s[j] = s[j], s[i]
        permutation(s,i+1)
        s[i], s[j] = s[j], s[i] 
        
        
permutation(["a","b","c"],0) 


        