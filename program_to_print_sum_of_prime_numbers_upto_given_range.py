import math
a,b=map(int,input().split())
b=b+1
l=[1]*b
x=int(math.sqrt(b))
l[0]=l[1]=0
for i in range(2,x+1):
    if l[i]==1:
        for j in range(i*i,b,i):
            l[j]=0
z=[]
s=0
for i in range(a,b):
    if l[i]==1:
        s=s+i
print(s)
