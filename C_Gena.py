n  =  int(input())
t1 = list(map(int,input().split()))

m =  int(input())
t2 = list(map(int,input().split()))

i,j=0,0
t1 = sorted(t1)
t2  = sorted(t2)
count =0

while i<n and j<m:
    if abs(t1[i]-t2[j])<=1:
        count+=1
        i+=1
        j+=1
    else:
        if t1[i]>t2[j]:
            j+=1
        else:
            i+=1


print(count)