nn=int(input())
l=[int(x) for x in input().split()]
for i in range(0,len(l)-1):
    if l[i]>l[i+1]:
        print(i)