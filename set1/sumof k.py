n,k=map(int,input().split())
l=[int(x) for x in input().split()]
sum=0
for i in range(0,k):
	sum+=l[i]
print(sum)