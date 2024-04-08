
from collections import defaultdict

for _ in range(int(input())):
    mp  = defaultdict(int)
    vmp  = defaultdict(int)
    unwantedv = defaultdict(int)

    
    n = int(input())
    matrix =[]


    i,j=0,n-1
    dzero,done =0,0 
    vzero,vone=0,0
    middle =""
    for x in range(n):
        s = input()
        matrix.append(s)
        mp[s[i]]+=1
        mp[s[j]]+=1
        if n%2:
            vmp[s[n//2]]+=1
        else:
            vmp[s[n//2]]+=1
            vmp[s[(n-1)//2]]+=1

        done += s.count("1")-int(s[i])-int(s[j])
        dzero =(s.count("0"))
        vzero = s.count("0")
        vone +=s.count("1")
        if s[i]=="0":
            dzero-=1
        if s[j]=="0":
            dzero-=1

        if x==(n)//2:
            middle =s[i]
        i+=1
        j-=1
        done =max(done,0)
        dzero = max(dzero,0)
    

    if n%2:
        mp[middle]-=1
        for j in range(n):
            if j!=n//2:
                vmp[matrix[(n)//2][j]]+=1
        for i in range(n):
            for j in range(n):
                if j!=n//2 and i!=n//2:
                    unwantedv[matrix[i][j]]+=1

    else:
        for j in range(n):
            if j!=n//2 and j!=(n-1)//2:
                vmp[matrix[(n-1)//2][j]]+=1
                vmp[matrix[(n)//2][j]]+=1
        for i in range(n):
            for j in range(n):
                if j!=n//2 and i!=n//2 and i!=(n-1)//2 and j!=(n-1)//2:
                    unwantedv[matrix[i][j]]+=1
    





    part1 =  min(mp["0"],mp["1"])+ min(vone,vzero)
    part2  = min(vmp["0"],vmp["1"])+min(unwantedv["1"],unwantedv["0"])
    # print(min(part1,part2))
    print(mp["0"],mp["1"],vone,vzero)
