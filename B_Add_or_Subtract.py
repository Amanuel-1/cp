for _ in range(int(input())):
    a,b,c  = list(map(int,input().split()))

    if a-b==c:
        print("-")
    else:
        print("+")