l = input()
dic = {}
for i in l:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
max = dic[l[0]]
max_char = l[0]
for i in dic:
    if dic[i]>max:
        max = dic[i]
        max_char = i
print(max,max_char
