n = int(input())
dic = {}
for i in range(n):
    k = input().split()
    dic[k[0]] = k[1]
for i in range(n):
    try:
        print(dic[input()])
    except:
        print("No result found")
