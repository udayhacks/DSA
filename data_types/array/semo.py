for i in range(int(input())):
    n, q = map(int,input().split())
    k = list(map(int, input().split()))
   
    for j in range(q):
        
        
        l , r = map(int,input().split())
        for i in range(l-1,r,2):
              k[i] = k[i]+1

        for i in range(l,r,2):
            k[i] = k[i]-1

        print(*k)
       
    print(sum(k))
                