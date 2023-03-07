def bubble_sort(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr)-i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]   
                count += 1   
            #print(*arr) 
        if count < 1:
            return print(*arr)
            
    return print(*arr)






l = [1,2,3,4]
n = len(l)
bubble_sort(l)
            