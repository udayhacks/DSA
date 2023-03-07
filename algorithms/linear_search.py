def  Nlinear_search(arr, n, x):
    for i in range(n):
        if arr[i] == x :
            return i
        
    return -1 




def Rlinear_search(arr,n,x):
    if n ==0:
        return -1
    elif arr[n-1] == x :
        return n-1
    else:
        return Rlinear_search(arr,n-1,x)


if __name__ == "__main__":
    

    a = [1,2,3,4,52,3,2,3]
    
    print("O(n) , O(1)")
    print(Nlinear_search(a,len(a),52))
    
    
    print("O(n), O(n)")
    
    print(Rlinear_search(a,len(a),52))