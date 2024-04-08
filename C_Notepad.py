for _ in range(int(input())):
    n=int(input())
    s =input()
    ans="NO"
    for i in range(len(s)-1):
        if s.count(s[i]+s[i+1])>1:
            ans="YES"
            break
    
    print(ans)
