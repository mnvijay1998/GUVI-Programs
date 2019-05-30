a,b=map(int,input().split())
t=a*b
k=t**0.5
if k**2==t:
	print("yes")
else:
	print("no")