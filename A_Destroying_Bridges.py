for _ in range(int(input())):
    n,k =  list(map(int,input().split()))
    if k>=(n-1):
        print(1)
    else:
        print(n)
