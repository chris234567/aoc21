with open("C:/Users/Chris/VSCodeProjects/AoC21/src/input/day07.txt") as f:
    l = f.readlines()

l = [int(i) for i in l[0].replace("\n", "").split(",")]

def solve(part1 = False):
    c = {}
    s = []

    for r in range(min(l), max(l)):
        if r not in s:
            s.append(r)

            for k in l:
                if not c.get(r):
                    c[r] = 0

                n = abs(r - k)

                if part1:
                    c[r] += n
                    continue

                c[r] += int(n * (n + 1) / 2)

    return c[min(c, key=c.get)]

print("solution to part 1: {}".format(solve(True)))
print("solution to part 2: {}".format(solve()))

