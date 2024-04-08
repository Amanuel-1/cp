from collections import defaultdict
mp =defaultdict(int)
for _ in range(int(input())):
    s =input()

    if s not in mp:
        print("OK")
    else:
        print(s+str(mp[s]))
    mp[s]+=1
