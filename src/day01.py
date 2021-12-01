with open("C:/Users/Chris/VSCodeProjects/AoC21/src/input/day01.txt") as f:
    l = list(map(int, f.readlines()))

# part 1

c1 = 0

for i in range(1, len(l)):
    if l[i] > l[i - 1]:
        c1 += 1

print(f"solution to part 1: {c1}")

# part 2

c2 = 0

for i in range(2, len(l) - 1):
    if l[i - 1] + l[i] +  l[i + 1] > l[i] +  l[i - 1] + l[i - 2] :
        c2 += 1

print(f"solution to part 1: {c2}")