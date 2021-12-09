with open("C:/Users/Chris/VSCodeProjects/AoC21/src/input/day06.txt") as f:
    l = f.readlines()


def solve(d):
    #day 0  1  2  3  4  5  6  7  8
    r = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in l[0].replace("\n", "").split(","):
        r[int(i)] += 1

    for _ in range(d):
        a = r[0]
        r = [r[1], r[2], r[3], r[4], r[5], r[6], r[7] + a, r[8], a]

    return sum(r)


print("solution to part 1: {}".format(solve(80)))
print("solution to part 2: {}".format(solve(256)))
