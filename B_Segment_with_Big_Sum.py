n,s  =  list(map(int,input().split()))
lst = list(map(int,input().split()))
sum_ = 0
mn=float('inf')
j=0
for i in range(n):
    while sum_<s and j<n:
        # print(j)
        sum_+=lst[j]
        j+=1
    print(sum_,i,j)
    mn= min(mn,j-i+1)
    # print(sum_,i,j)
    sum_-=lst[i]


print(mn)