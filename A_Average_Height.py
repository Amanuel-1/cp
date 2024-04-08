for _ in range(int(input())):
    n =  int(input())
    lst  = list(map(int,input().split()))
    even,odd  = [],[]

    for c in lst:
        if c%2:
            odd.append(c)
        else:
            even.append(c)
    

    print(*(odd+even))


    
