with open("input.txt", "r") as f:
    f = f.readlines()
f = list(map(lambda x:x.strip(), f))
length, height = len(f[0]), len(f)
vissebleTrees = length * 2 + height * 2 - 4

def isVissbel(row, col, height):
    left, right, up, down = 0, 0, 0, 0
    #check left
    for i in range(col)[::-1]:
        if f[row][i] >= height:
            left = col-i
            break
    else:
        left = col
    #check right
    for i in range(length)[col+1:]:
        if f[row][i] >= height:
            right = i-col
            break
    else:
        right = length-col-1
    #check up
    for i in range(row)[::-1]:
        if f[i][col] >= height:
            up = row - i
            break
    else:
        up = row
    #check down
    for i in range(length)[row+1:]:
        if f[i][col] >= height:
            down = i - row
            break
    else:
        down = length-row-1
    return left * right * up * down

score = 0

for row, i in enumerate(f[1:-1]):
    row += 1
    for col, j in enumerate(i[1:-1]):
        col += 1
        x = isVissbel(row, col, f[row][col])
        if x > score:
            score = x

print(score)
