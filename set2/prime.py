n=int(input())
fl=0
for i in range(2,n):
	if n%i==0:
		f=-1
		break
		
if fl==0 and n>1:
	print("yes")
else:
	print("no")