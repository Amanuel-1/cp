def check(st):
    ref ="abacaba"


    for i in range(len(ref)):
        if st[i]!="?" and st[i]!=ref[i]:
            return False
    return True

for _ in range(int(input())):
    found =False
    n=int(input())
    s =input()
    count=0
    for i in range(len(s)-6):
        if s[i:i+7]=="abacaba":

            count+=1
    if count>1:
        print("No")
        continue
    elif count==1:
        s= s.replace("?","a",len(s))
        print("Yes")
        print(s)
        continue
    else:



        i=0
        while i<n-6:
            if check(s[i:i+7]):
                found=True
                s = s[:i]+"abacaba"+ (s[i+7:])
                print(s)
                    
                break
            else:
                i+=1

        if count>1 or (not found and "abacaba" not in s):
            print("No")
        elif found:
            count=0
            for i in range(len(s)-6):
                if s[i:i+7]=="abacaba":
                    count+=1

            if count>1:
                print("No")
            else:
                print("Yes")
                s=s.replace("?","a",len(s))
                print(s)






        