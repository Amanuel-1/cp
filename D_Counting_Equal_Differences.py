from collections import defaultdict
for _ in range(int(input())):
    n= int(input())
    lst = list(map(int,input().split()))
    mp =defaultdict(int)
    count=0

    for i in range(len(lst)):
        val = lst[i]-i
        count+=mp[val]
        mp[val]+=1

    print(count)
