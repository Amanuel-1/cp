from collections import defaultdict
n  = int(input())
graph  = defaultdict(list)


def search(node,depth=1,max_=1):
    if not graph[node]:
        return depth
    else:
        for child in graph[node]:
            max_  = max(max_,search(child,depth+1))

    
        return max_

for i in range(1,n+1):
    graph[int(input())].append(i)

min_group  = -float('inf')


for i in graph[-1]:
    min_group = max(min_group,search(i))

print(min_group)




