n = int(input())
lst  =  list(map(int,input().split()))

odds,even =[],[]

for v in lst:
    if v%2!=0:
        odds.append(v)
    else:
        even.append(v)

odds = sorted(odds)
print()
sum_odds  = 0
if len(odds)%2:
    sum_odds =sum(odds[1:])
else:
    sum_odds = sum(odds)

print(sum(even)+sum_odds)