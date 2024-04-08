for _ in range(int(input())):
    s  =  input()
    sample  = "codeforces"

    count = 0

    for i in range(10):
        if s[i]!=sample[i]:
            count+=1
    
    print(count)