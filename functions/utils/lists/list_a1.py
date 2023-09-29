players = ["Matthias Schmitt", "Felix Holzmann",
           "Sabrina Eggers", "Sebastian Wolf", "Niklas Eisenbaum"]
place = int(input('Welche Platzierung soll ausgegeben werden? '))
print(f"Platzierung {place}: {players[place - 1]}")
print(f"Tielnehmerzahl: {len(players)}")
