with open("input.txt", "r") as f:
    f = f.readlines()
f = map(lambda x:x.strip().split(","), f)
score = 0

for i in f:
    s1, s2 = i[0].split("-"), i[1].split("-")
    s1 = list(map(lambda x:int(x), s1))
    s2 = list(map(lambda x: int(x), s2))
    if s1[0] <= s2[0] and s1[1] >= s2[1]:
        score += 1
        continue
    elif s2[0] <= s1[0] and s2[1] >= s1[1]:
        score += 1
        continue
print(score)