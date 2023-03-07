def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
     
        while(j>= 0 and arr[j] > key):
            #k = arr[j]
            arr[j+1] = arr[j]
            #print(*arr)
            
            
            j -= 1
        arr[j+1] = key 
        #print(arr)  
    return print(*arr)
        
    





p = [5,3,4,32,1]
print(*p) 
insertion_sort(p)
