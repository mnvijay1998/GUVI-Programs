sn,ln=map(int,input().split())
if sn%2==0:
	sn+=1
else:
	sn+=2
for i in range(sn,ln,2):
	print(i,end=' ')