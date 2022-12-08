with open("input.txt", "r") as f:
    f = f.readlines()

boxes = [[], [], [], [], [], [], [], [], []]
for startIndex, i in enumerate(f):
    if i == "\n":
        break
    index = -1
    for j in i[1::4]:
        index += 1
        if j.isalpha():
            boxes[index].insert(0, j)
        else:
            continue

for i in f[startIndex+1:]:
    x = i.strip().split(" ")
    MOVE, FROM, TO = int(x[1]), int(x[3])-1, int(x[5])-1
    for j in range(MOVE):
        boxes[TO].append(boxes[FROM][-1])
        boxes[FROM].pop(-1)

for i in boxes:
    if i == []:
        continue
    print(i[-1], end="")