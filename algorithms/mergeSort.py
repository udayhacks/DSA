def merge(arr, l ,m, h) :
    i = j = 0 
    k = l 
    lf= arr[l:m+1] 
    rt = arr[m+1:h+1]
    while i < len(lf) and j < len(rt) :
        if lf[i] <= rt[j]:
            arr[k] = lf[i]
            i+=1
            k +=1
        else :
            arr[k] = rt[j]
            j+=1
            k+=1  
    while i <len(lf) :
        arr[k] = lf[i]
        i+=1
        k+=1
    while j < len(rt):
        arr[k] = rt[j]
        j+=1
        k+=1
      
      
      
def mergeSort(arr,l,h):
    if h>l :
        mid = (l+h)//2
        mergeSort(arr,l,mid)
        mergeSort(arr,mid+1,h)
        merge(arr,l, mid,h)  
      
      
      

 
        
ar = [9,7,8,4,2]


merge([1,4,9,2,8,5],0,2,5)



"""
arr = [10, 5, 30, 15, 7]
h = len(ar)
mergeSort(arr,0,h)
print(arr)"""