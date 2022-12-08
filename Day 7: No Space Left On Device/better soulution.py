with open("input.txt", "r") as f:
    f = f.readlines()
f = map(lambda x: x.strip(), f)
path = ""
temp = 0
ls = False
all = {}

def setValue(path):
    x = path.split(" ")
    for i in range(len(x)-1):
        path = " ".join(path.split(" ")[:-1])
        all[path] += temp

for i in f:
    x = i.split(" ")
    if ls:
        c = x[0]
        if c == "$":
            ls = False
            all[path] = temp
            setValue(path)
            temp = 0
        elif c != "dir" and ls:
            temp += int(c)
            continue

    if x[0] == "$":
        if x[1] == "cd":
            if x[2] == "..":
                path = " ".join(path.split(" ")[:-1])
            else:
                if x[2] == "/":
                    path += f"{x[2]}"
                else:
                    path += f" {x[2]}"
        elif x[1] == "ls":
            ls = True
else:
    ls = False
    all[path] = temp
    setValue(path)
    temp = 0

score = 0
for i in all:
    x = all[i]
    if x <= 100000:
        score += x

spaceNeeded = 30000000-(70000000-all["/"])

values = []
for i in all:
    values.append(all[i])
values.sort()
score2 = 0
for i in values:
    if i >= spaceNeeded:
        score2 = i
        break
print(f"Part 1: {score}")
print(f"Part 2: {score2}")