draws = []
for _ in range(5):
    draws.append(int(input("Gezogene Losnummer: ")))
print("-- Gewinnlose --")
print(*draws, sep="\n")
