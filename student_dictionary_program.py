dic = {}
n = int(input("Enter Number of students"))
for i in range(n):
    stunum = int(input("Enter Student Number: "))
    k = {
        "sname" : input("Enter Student Name: "),
        "group" : input("Enter Student Group: "),
        "college" : input("Enter Student College: "),
        "branch" : input("Enter Student Branch: "),
        "phone" : input("Enter Phone Number: ")
    }
    dic[stunum] = k
print(dic[int(input("Enter Student Number: "))])
