with open("input.txt", "r") as f:
    f = f.readlines()
f = list(map(lambda x: x.strip(), f))

score = 0
for index, i in enumerate(f[::3]):
    index *= 3
    for j in i:
        if j in f[index+1] and j in f[index+2]:
            if j.isupper():
                score += ord(j) - 38
            else:
                score += ord(j) - 96
            break
print(score)