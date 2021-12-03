with open("C:/Users/Chris/VSCodeProjects/AoC21/src/input/day03.txt") as f:
    l = f.readlines()

def most_common(l: list, p: int):
    a = b = 0

    for i in l:
        if i[p] == "1":
            a += 1
        else:
            b += 1

    return "1" if a >= b else "0"

# part 1

g = e = ""

for p in range(len(l[0]) - 1):
    m = most_common(l, p)

    if m == "1":
        g += "1"
        e += "0"
    else:
        g += "0"
        e += "1"

print(f"solution to part 1: {int(g, 2) * int(e, 2)}")

# part 2

a = b = 0

o1 = l
c1 = l
o2 = []
c2 = []

for p in range(len(l[0]) - 1):
    m = most_common(o1, p)

    if len(o1) > 1:
        for i in o1:
            if m == i[p] == "1":
                o2.append(i)
            elif m == i[p] == "0":
                o2.append(i)     
            
        o1 = o2
        o2 = []

    if len(c1) > 1:
        m = most_common(c1, p)

        for i in c1:
            if m != i[p] == "0":
                c2.append(i)
            elif m != i[p] == "1":
                c2.append(i)

        c1 = c2
        c2 = []

print("solution to part 1: {}".format(
    int(o1[0].replace("\n", ""), 2) * 
    int(c1[0].replace("\n", ""), 2))
)