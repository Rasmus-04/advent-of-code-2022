with open("input.txt", "r") as f:
    f = f.readlines()
f = list(map(lambda x:x.strip(), f))
length, height = len(f[0]), len(f)
vissebleTrees = length * 2 + height * 2 - 4

def isVissbel(row, col, height):
    x = 0
    #check left
    for i in range(col):
        if f[row][i] >= height:
            x += 1
            break
    #check right
    for i in range(length)[col+1:]:
        if f[row][i] >= height:
            x += 1
            break
    #check up
    for i in range(row):
        if f[i][col] >= height:
            x += 1
            break
    #check down
    for i in range(length)[row+1:]:
        if f[i][col] >= height:
            x += 1
            break
    if x == 4:
        return 1
    return 0

for row, i in enumerate(f[1:-1]):
    row += 1
    for col, j in enumerate(i[1:-1]):
        col += 1
        if not isVissbel(row, col, f[row][col]):
            vissebleTrees += 1

print(vissebleTrees)