
from math import sqrt
def jump_search(arr,n,x):
    parts = int(sqrt(n))
    start =0
    while(arr[parts]<x):
        start = parts
        parts += sqrt(n)
        
        if parts >= n :
            return None
        
        while(arr[start]<x):
            start+=1
            if start == parts:
                return None
            
        if arr[start] == x :
            return start 
        
        
        
        
        
a = [1,2,3,4,5,6,7,8,9,10,12,13]  
x = 13
n = len(a)
i = jump_search(a, n, x)
print(a[i])


