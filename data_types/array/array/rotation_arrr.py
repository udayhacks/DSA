def rotation(arr, n , r ):
    return arr[r:n]+arr[:r]
    print(*arr)
    


if __name__ == '__main__':
    n = 8
    l = [1,2,3,4,5,6,7,8]
    r = 3
    (rotation(l,n,r))
   