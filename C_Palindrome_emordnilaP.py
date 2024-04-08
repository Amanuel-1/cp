from collections import defaultdict
for _ in range(int(input())):
    n= int(input())
    lst = list(map(int,input().split()))
    # print(lst)



    answer  = "NO"
    if len(lst)==3:
        if lst[0]==lst[-1]:
            answer="YES"
            

    else:
        mp = defaultdict(int)
        for i in range(len(lst)):
            if lst[i] in mp and i-mp[lst[i]] >1:
                answer="YES"
                break
            if lst[i] not in mp:
                mp[lst[i]]=i
    print(answer)