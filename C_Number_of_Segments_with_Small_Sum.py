n,s  =  list(map(int,input().split()))
lst = list(map(int,input().split()))
sum_ = 0
i=0

count = 0

for j in range(n):
    sum_+=lst[j]

    while sum_>s and i<j:
        sum_-=lst[i]
        i+=1
    
    count+=j-i+1

print(count)