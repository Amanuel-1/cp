from collections import defaultdict
for _ in range(int(input())):
    n= int(input())
    lst = list(map(int,input().split()))
    mp =defaultdict(int)
    reversed =False
    isSorted =False
    inc,dec =True,True
    same = True
    newlst  = []
    for i in range(len(lst)-1):
        mp[lst[i]]+=1
        if lst[i]>lst[i+1]:
            inc=False
        if lst[i]<lst[i+1]:
            dec=False
        if lst[i]!=lst[i+1]:
            same=False

    mp[lst[-1]]+=1
    if inc or same:
        print(0)
    elif dec:
        print(max(lst))
    elif len(mp)==2:
        mn,mx =lst[i],lst[i+1]
        if (min(lst)+max(lst))//2 not in [min(lst),max(lst)]:
            print((mn+mx)//2)
    else:
        print(-1)
        
