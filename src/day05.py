with open("C:/Users/Chris/VSCodeProjects/AoC21/src/input/day05.txt") as f:
    l = f.readlines()

def solve(with_diagonal = False):

    m = {}

    for i in l:
        c = i.replace("\n", "").split(" ")

        x1, y1 = [int(g) for g in c[0].split(",")]
        x2, y2 = [int(g) for g in c[2].split(",")]

        if x1 == x2 or y1 == y2:
            a1 = max(x1, x2)
            a2 = min(x1, x2)

            b1 = max(y1, y2)
            b2 = min(y1, y2)

            for x in range(a1 - a2 + 1):
                for y in range(b1 - b2 + 1):
                    if m.get((a2 + x, b2 + y)):
                        m[(a2 + x, b2 + y)] += 1
                    else:
                        m[(a2 + x, b2 + y)] = 1

        elif with_diagonal:
            a1 = max(x1, x2)
            a2 = min(x1, x2)

            for d in range(a1 - a2 + 1):
                if m.get((x1 + d * (1 if x2 >= x1 else -1), y1 + d * (1 if y2 >= y1 else -1))):
                    m[(x1 + d * (1 if x2 >= x1 else -1), y1 + d * (1 if y2 >= y1 else -1))] += 1
                else:
                    m[(x1 + d * (1 if x2 >= x1 else -1), y1 + d * (1 if y2 >= y1 else -1))] = 1

    r = 0

    for k in m:
        if m[k] > 1:
            r += 1

    if not with_diagonal:
        print("solution to part 1: {}".format(r))
        return
    
    print("solution to part 2: {}".format(r))


solve()  # part 1
solve(True)  # part 2
