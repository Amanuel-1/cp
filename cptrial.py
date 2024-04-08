for _ in range(int(input())):
    n, p, l, t = list(map(int, input().split()))
    cntTasks = (n + 6) // 7

    def calc(k):
        return k * l + min(cntTasks, 2 * k) * t

    lf = 0
    rg = n

    while rg - lf > 1:
        mid = (lf + rg) // 2
        if calc(mid) >= p:
            rg = mid
        else:
            lf = mid

    print(n - rg)
