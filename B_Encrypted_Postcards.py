for _ in range(int(input())):
    n = int(input())
    s  =  input()
    answer = []
    cur  = s[0]
    i=1

    while i<n:
        if s[i]==cur:
            if i+1<n:
                answer.append(cur)
                cur=s[i+1]
                i+=1
        i+=1
    answer.append(cur)
    print("".join(answer))



