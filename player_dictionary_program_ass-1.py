player = []
n = int(input("Enter Number of players: "))
for i in range(n):
    l = {}
    l['pno'] = input("Enter Player Number: ")
    l['pname'] = input("Enter Player Name: ")
    player.append(l)
print(player)
