with open("day1.txt", "r") as f:
    f =f.readlines()
p = len(f)
f = map(lambda x: x.strip(), f)

mest = []
current = 0

def calc():
    if len(mest) < 3:
        mest.append(current)
    else:
        if current > min(mest):
            mest[mest.index(min(mest))] = current

for index, i in enumerate(f):
    if i == "":
        calc()
        current = 0
        continue
    current += int(i)
    if index == p-1:
        calc()

print("Svar för första:", max(mest))
print("Svar för andra:", sum(mest))