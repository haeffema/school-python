def show_players(players):
    print(*players, sep="\n")


def insert_player(players):
    name = input("Spielername: ")
    index = int(input("Index: "))
    return players[:index] + [name] + players[index:]


players = insert_player(["Bob", "Fritz", "Hans", "Kai", "Kurt", "Paul"])
show_players(players)
