def selection_sort (arr):
    
    for i in range(len(arr)):
        m = i
        for j in range(i +1, len(arr)):
            if arr[m] > arr[j]:
                m = j 
        
        arr[i], arr[m] = arr[m], arr[i]
        
        
    return print(*arr)
        
        
l = [1,3,42,5,3]
selection_sort(l)


