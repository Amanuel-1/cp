b= int(input())
boys =  list(map(int,input().split()))
g =  int(input())
girls  =  list(map(int,input().split()))

boys,girls =  sorted(boys),sorted(girls)

i,j  = 0,0
count  =0

while i<len(boys) and j<len(girls):
    if abs(boys[i]-girls[j])<=1:
        count+=1
        i+=1
        j+=1
    else:
        if boys[i]<girls[j]:
            i+=1
        else:
            j+=1
    
print(count)
