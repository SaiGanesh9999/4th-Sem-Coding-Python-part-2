l = list(map(int,input().split()))
d = {}
for i in l:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)
m = d[l[0]]
mm = d[l[0]]
for i in d:
    if d[i] < m:
        m = i
    if d[i] > mm:
        mm=i
print(abs(mm-m))
