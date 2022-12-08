with open("input.txt", "r") as f:
    f = f.readlines()

f = f[0].strip()

#x = 4 för part 1
#x = 4

# x = 14 för part 2
x = 14

recent = []
for index, j in enumerate(f):
    if len(recent) < x:
        recent.append(j)
        continue
    if len(set(recent)) == x:
        print(index)
        break
    else:
        recent.append(j)
        recent.pop(0)