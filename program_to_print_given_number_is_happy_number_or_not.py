def happ(n):
    s=0
    while(n!=0):
        r=n%10
        s=s+(r*r)
        n=n//10
    if s==1:
        return True
    else:
        if s==2 or s==3 or s==4 or s==5 or s==6 or s==8 or s==9:
            return False
        else:
            return True
n= int(input())
s=0
if (happ(n)):
    print('happy')
else:
    print('not happy')
