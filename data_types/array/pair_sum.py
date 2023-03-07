# with sum equals to x.
def su(arr, n ):
    k = 0
    arr.sort()
    for i in range(len(arr)):
        for j in range(len(arr)):
                if arr[i]+arr[j] == n :
                    k +1
                    return True ,k             
            

    
    
    
                
            
            
arr = [11, 15, 6, 8, 9, 10,16]
n= 16 
print(su(arr,n))
 