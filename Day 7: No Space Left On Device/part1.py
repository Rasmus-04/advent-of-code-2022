with open("input.txt", "r") as f:
    f = f.readlines()
f = list(map(lambda x: x.strip(), f))
path = ""

temp = 0
ls = False

all = {}

for index, i in enumerate(f):
    x = i.split(" ")

    if ls:
        c = x[0]
        if c != "dir":
            temp += int(c)
        if index+1 > len(f)-1 or f[index+1].split(" ")[0] == "$":
            ls = False
            all[path] = temp
            temp = 0

    if x[0] == "$":
        if x[1] == "cd":
            if x[2] == "..":
                path = " ".join(path.split(" ")[:-1])
                pass
            else:
                if x[2] == "/":
                    path += f"{x[2]}"
                else:
                    path += f" {x[2]}"
        elif x[1] == "ls":
            ls = True


def calc_value(pathh):
    score = 0
    for i in all:
        if i[:len(pathh)] == pathh:
            score += all[i]
    return score

score = 0
for i in all:
    value = calc_value(i)
    if value <= 100000:
        score += value

print(score)