for _ in range(int(input())):
    s = input()
    answer =""
    answer+=s[0]
    
    for i in range(1,len(s)-1,2):
        answer+=s[i]
    
    answer+=s[-1]

    print(answer)