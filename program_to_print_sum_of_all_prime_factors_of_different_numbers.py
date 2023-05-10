import math
t=int(input())
s=0
while(t>0):
    n=int(input())
    while(n%2==0):
        s=s+2
        n=n//2
    for i in range(3,int(math.sqrt(n))+1,2):
        while(n%i==0):
            s=s+i
            n=n//i
    if n>2:
        s=s+n
t=t-1
print(s)
