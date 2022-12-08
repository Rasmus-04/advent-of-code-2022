with open("input.txt", "r") as f:
    f = f.readlines()
f = map(lambda x: x.strip().split(" "), f)
score = 0

"""
A = Rock
B = Papper
C = Scissors

X = Rock
Y = Papper
Z = Scissors

Rock = 1
Papper = 2
Scissors = 3
"""

for i in f:
    a = i[0]
    b = i[1]
    if a == "A":
        if b == "Y":
            score += 2 + 6
        if b == "X":
            score += 1 + 3
        if b == "Z":
            score += 3 + 0
    if a == "B":
        if b == "Y":
            score += 2 + 3
        if b == "X":
            score += 1 + 0
        if b == "Z":
            score += 3 + 6
    if a == "C":
        if b == "Y":
            score += 2 + 0
        if b == "X":
            score += 1 + 6
        if b == "Z":
            score += 3 + 3
print(score)