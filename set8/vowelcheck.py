n=input()
f=0
l=['a','e','i','o','u','A','E','I','O','U']
for i in n:
	if i in l:
		f=1
		break
if f:
	print("yes")
else:
	print("no")