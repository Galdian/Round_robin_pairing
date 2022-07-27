players_num = int(input("What is the number of players? "))
players_list = []
a = 1
for player in range(players_num):
    players_list.append(a)
    a += 1

if not len(players_list) % 2 == 0:
    players_list.append(0)
    print("I've added a dummy player for pairing purposes!")
print(f"Players list: {players_list}")
players_num = len(players_list)

rounds = players_num - 1
pairs = int(players_num/2)

for r in range(rounds):
    print(f"Pairings for round {r+1}:")
    first_paired_player = 0
    second_paired_player = rounds
    for p in range(pairs):
        print(f"{players_list[first_paired_player]} vs {players_list[second_paired_player]}")
        first_paired_player += 1
        second_paired_player -= 1
    player_moved = players_list[rounds]
    players_list.insert(1, player_moved)
    players_list.pop()




