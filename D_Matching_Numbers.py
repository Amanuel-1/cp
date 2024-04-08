for _ in range(int(input())):
    n=int(input())

    if n%2==0:
        print("No")
    else:
        # o=1
        # sign=1

        # for i in range(2*n,n,-1):
        #     if o>n:
        #         o=
        #     print(n,o)
        #     o+=2
        e = n//2 *2
        print("Yes")
        x=2*n
        for i in range(1,n+1,2):
            print(i,x)
            x-=1
        for i in range(2,n,2):
            print(x,i)
            x-=1

