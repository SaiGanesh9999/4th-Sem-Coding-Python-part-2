n=1001
pf=[i for i in range(n)]
for i in range(1,n):
    pf[i]=pf[i-1]+i
l,r=map(int,input().split())
print(pf[r]-pf[l-1])
