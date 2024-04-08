n,s  = list(map(int,input().split()))
lst  =list(map(int,input().split()))

i=0
sum_=0
mx =0
for j in range(len(lst)):
    sum_+=lst[j]
    if sum_>s:
        while sum_>s and i<=j:
            sum_-=lst[i]
            i+=1
    mx =max(mx,j-i+1)


print(mx)
