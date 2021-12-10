with open("C:/Users/Chris/VSCodeProjects/AoC21/src/input/day10.txt") as f:
    l = [_.replace("\n", "") for _ in f.readlines()]

o = ["(", "[", "{", "<"]
c = [")", "]", "}", ">"]

f = []
corrupted = []
score_all = []

for i in l:
    stack = []

    for b in i:
        if b in o:
            stack.append(b)
        else:
            if c[o.index(stack[-1])] != b:
                f.append(b)
                corrupted.append(i)
                break

            stack.pop()
    else:
        score = 0
        stack.reverse()

        for k in stack:
            score = score * 5 + o.index(k) + 1
        
        score_all.append(score)


d = {")": 3, "]": 57, "}": 1197, ">": 25137}
s = 0

for i in d:
    s += f.count(i) * d[i]

score_all.sort()

print("solution to part 1: {}".format(s))
print("solution to part 2: {}".format(score_all[len(score_all) // 2]))
