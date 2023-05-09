import math
a,b=map(int,input().split())
l=[1]*b
x=int(math.sqrt(b))
l[0]=l[1]=0
for i in range(2,x+1):
    if l[i]==1:
        for j in range(i*i,b+1,i):
            l[j]=0
for i in range(a+1,b):
    if l[i]==1:
        print(i,end=' ')
