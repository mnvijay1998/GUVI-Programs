import math
n=int(input())
l=[int(x) for x in input().split()]
l.sort()
med=math.ceil(len(l)/2)
print(l[med-1])