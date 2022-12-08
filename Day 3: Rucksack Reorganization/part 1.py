with open("input.txt", "r") as f:
    f = f.readlines()
f = map(lambda x: x.strip(), f)

score = 0
for i in f:
    compartment1, compartment2 = i[:int(len(i)/2)], i[int(len(i)/2):]
    for j in compartment1:
        if j in compartment2:
            if j.isupper():
                score += ord(j)-38
            else:
                score += ord(j)-96
            break
print(score)