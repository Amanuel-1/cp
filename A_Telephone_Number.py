for _ in range(int(input())):
    n = int(input())
    number  = input()
    answer  =  "YES"
    if "8" not in number:
        print("NO")
        continue
    resedue=n-number.index("8")
    if resedue<11:
        answer="NO"
    

    print(answer)