 
  
def reverseArray(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end-1
    print(*arr)
# Function to left rotate arr[] of size n by d

  
def leftRotate(arr, d,n):
  
    if d == 0:
        return
    print("REVESAL ALGORITHM ")
    print("step -1 :" ,end = " ")
    reverseArray(arr, 0, d-1)
    print("step -2 :",end = " ")
    reverseArray(arr, d, n-1)
    print("step -3 :",end = " ")
    reverseArray(arr, 0, n-1)



# Driver function to test above functions
arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
d = 2

leftRotate(arr, d , n)


