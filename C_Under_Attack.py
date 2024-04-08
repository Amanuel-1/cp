from collections import defaultdict
for _ in range(int(input())):
    n,m = list(map(int,input().split()))
    mp =defaultdict(int)
    mp2 =defaultdict(int)
    matrix =[]
    for i in range(n):
        row =list(map(int,input().split()))
        matrix.append(row)
        for j in range(m):
            mp[i+j]+=row[j]
            mp2[j-i]+=row[j]
    mx =0

    for i in range(n):
        for j in range(m):
            mx =max(mx,mp[i+j]+mp2[j-i]-matrix[i][j])
    
    

    print(mx)