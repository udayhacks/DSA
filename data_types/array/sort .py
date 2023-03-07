l = [1,2,3,4,5,6,7,8]
n = 7
p =[]
for i in range(int(n/2+1)):
    if len(l) == 1 :
        p.append(max(l)) 
    else:    
        p.append(max(l))
        p.append(min(l))
        l.remove(max(l))
        l.remove(min(l))  
        
        
print(*p)


"""
sort first max and first least in the pattern sort 
output :
81726354
"""