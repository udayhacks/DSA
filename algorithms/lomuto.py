def lomuto(arr, v) :
    n = len(arr)
    arr[n-1] ,arr[v] = arr[v],arr[n-1] 
    j = -1
    l = 0 
    h = n-1
    
    
    
    for i in range(l,h) :
        if arr[i] <=arr[n-1]:
            j+=1
            arr[i] ,arr[j] = arr[j] , arr[i]
    arr[j+1] ,arr[n-1] = arr[n-1],arr[j+1]
    return j+1



arr= [10,80,30,90,50,70]
v = 2

lomuto(arr,4)
        