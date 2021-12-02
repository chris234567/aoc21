with open("C:/Users/Chris/VSCodeProjects/AoC21/src/input/day02.txt") as f:
    l = [i.replace("\n", "") for i in f.readlines()]

# part 1

p = 0
d = 0

for i in l:
    if i.startswith("f"):
        p += int(i[-1])
    elif i.startswith("d"):
        d += int(i[-1])
    else:
        d -= int(i[-1])

print(f"solution to part 1: {p * d}")

# part 2

p = 0
d = 0
a = 0

for i in l:
    if i.startswith("f"):
        d += a * int(i[-1])
        p += int(i[-1])
    elif i.startswith("d"):
        a += int(i[-1])
    else:
        a -= int(i[-1])

print(f"solution to part 2: {p * d}")
