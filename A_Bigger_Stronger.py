for _ in range(int(input())):
    n =int(input())

    lst = list(map(int,input().split()))

    lst = sorted(lst)
    answer ="YES"

    for i in range(n-1):
        if lst[i]==lst[i+1]:
            answer="NO"
            break
    

    print(answer)