"""def bs(a,k,l,h):
    
    a.sort()
    low = l
    high = h 
    mid = l+h // 2 
    
    
    while (low != high ): 
        
          mid = (low + high ) // 2
          if a[mid]  == k :
              return mid  
          if a[mid] > k :
              high = mid
              
          else :
              low = mid
              
              
              
              

     
l = [1,2,3,4,5,6]


print(l[bs(l,1,0,6)])
"""

for  i in range(int(input())):3
  n = int(input())
  if n >0 :
    for i in range(n):
      n = n-i
     
      if n <0:
        print(i-1)
        break
      if n == 0 :
        print(i)
        break 
  else:
    print(0)