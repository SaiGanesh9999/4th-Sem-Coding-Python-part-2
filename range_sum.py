t=int(input())#2
for i in range(t):#no of testcases(2)
    n=int(input())#5
    arr=list(map(int,input().split()))

    pf=[0]*(n+1)# 0 1  2  3  4  5
    for i in range(1,n+1):#i=6,6
        pf[i]=pf[i-1]+arr[i-1]
    q=int(input())#3
    while(q>0):
        l,r=map(int,input().split())
        print(pf[r]-pf[l-1])
        q=q-1


