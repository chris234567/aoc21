from math import prod

with open("C:/Users/Chris/VSCodeProjects/AoC21/src/input/day09.txt") as f:
    l = [y.replace("\n", "") for y in f.readlines()]
    
MAX_X = len(l[0]) - 1
MAX_Y = len(l) - 1

lows = []
visited = {}


def mark(r, coord):
    lows.append(int(r))

    visited[coord[0], coord[1]] = []
    mark_coords_non_9((coord[0], coord[1]), (coord[0], coord[1]), visited, True)


def mark_coords_non_9(source, coord, visited, start = False):
    # recursive mit list wo man schon war

    if coord[0] > MAX_X or coord[0] < 0 or coord[1] > MAX_Y or coord[1] < 0:  # koordinate ausserhalb
        return

    if not start:
        if int(l[coord[1]][coord[0]]) == 9 or coord in visited[source]:
            return
    
    visited[source].append(coord)

    mark_coords_non_9(source, (coord[0] + 1, coord[1]), visited)
    mark_coords_non_9(source, (coord[0] - 1, coord[1]), visited)
    mark_coords_non_9(source, (coord[0], coord[1] + 1), visited)
    mark_coords_non_9(source, (coord[0], coord[1] - 1), visited)


for y, k in enumerate(l):
    for x, r in enumerate(k):
        if x == 0:  # no left num
            if y == 0:  # no upper num
                if r < k[x + 1] and r < l[y + 1][x]:
                    mark(r, (x, y))

            elif y == len(l) - 1:
                if r < k[x + 1] and r < l[y - 1][x]:
                    mark(r, (x, y))

            else:
                if r < k[x + 1] and r < l[y - 1][x] and r < l[y + 1][x]:
                    mark(r, (x, y))

        elif x == len(k) - 1:  # no right num
            if y == 0:  # no upper num
                if r < k[x - 1] and r < l[y + 1][x]:
                    mark(r, (x, y))

            elif y == len(l) - 1:
                if r < k[x - 1] and r < l[y - 1][x]:
                    mark(r, (x, y))
            else:
                if r < k[x - 1] and r < l[y - 1][x] and r < l[y + 1][x]:
                    mark(r, (x, y))

        else:
            if y == 0:  # no upper num
                if r < k[x - 1] and r < k[x + 1] and r < l[y + 1][x]:
                    mark(r, (x, y))

            elif y == len(l) - 1:
                if r < k[x - 1] and r < k[x + 1] and r < l[y - 1][x]:
                    mark(r, (x, y))

            else:
                if r < k[x - 1] and r < k[x + 1] and r < l[y - 1][x] and r < l[y + 1][x]:
                    mark(r, (x, y))


print("solution to part 1: {}".format(sum(lows) + len(lows)))
print("solution to part 2: {}".format(prod(sorted([len(visited[k]) for k in visited], reverse=True)[:3])))
