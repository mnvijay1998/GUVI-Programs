p=int(input())
f=0
for i in range(2,p):
	if p%i==0:
		f=1
		break
if f==1 and p>1:
	print("yes")
else:
	print("no")