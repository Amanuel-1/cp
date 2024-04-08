for _ in range(int(input())):
    n = int(input())
    found = False
    for j in range(n):
        lst = list(map(int, input().split()))
        print(*lst, "  ", lst.count(0))

        if lst.count(0) == 1:
            found = True
            print("Yes")
            print(*lst)
            break
    if not found:
        print("No")
