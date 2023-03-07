"""

important in the interpolationSearch

       pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) *
                    (x - arr[lo]))
                    
                    
                    
                    
"""




 
def interpolationSearch(arr, lo, hi, x):
 
    # Since array is sorted, an element present
    # in array must be in range defined by corner
    if (lo <= hi and x >= arr[lo] and x <= arr[hi]):
 
        # Probing the position with keeping
        # uniform distribution in mind.
        pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) *
                    (x - arr[lo]))
 
        # Condition of target found
        if arr[pos] == x:
            return pos
 
        # If x is larger, x is in right subarray
        if arr[pos] < x:
            return interpolationSearch(arr, pos + 1,
                                       hi, x)
 
        # If x is smaller, x is in left subarray
        if arr[pos] > x:
            return interpolationSearch(arr, lo,
                                       pos - 1, x)
    return -1
 




        
a = [1,2,3,4,5,6,7,8,9,10,12,13]  
x = 12
n = len(a)
i = interpolationSearch(a , 0, n-1, x)
print(a[i],i)


      
        
    