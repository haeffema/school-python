throws = []
for counter in range(5):
    throws.append(int(input(f"Wurf {counter + 1}: ")))
print(f"Bester Wurf: {max(throws)}")
print(f"Schlechtester Wurf: {min(throws)}")
print(f"Durchschnittliche Punktzahl: {round(sum(throws) / len(throws), 2)}")
