n=list(input())
l=[]
for i in n:
    if i.isnumeric():
        l.append(i)
if l==[]:
    print()
else:
    for i in l:
        print(i,end='')