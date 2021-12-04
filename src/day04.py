with open("C:/Users/Chris/VSCodeProjects/AoC21/src/input/day04.txt") as f:
    l = f.readlines()

def get_unchecked_sum(boards, c):
    sum = 0
    for r in range(5):
        for q in range(5):
            if boards[c][g][r][q] not in checked:
                sum += int(boards[c][g][r][q])
    
    return sum


nums = l[0]
boards = {} 

for i in range(len(l) - 2):  # some cleaning
    if l[2 + i] == "\n":
        continue

    l[2 + i] = l[2 + i].replace("  ", " ").replace("\n", "")

    if l[2 + i][0] == " ":
        l[2 + i] = l[2 + i][1:]

for i in range(0, len(l) - 2, 6):
    boards[i] = [
        [
            l[2 + i].split(" "), 
            l[2 + i + 1].split(" "), 
            l[2 + i + 2].split(" "), 
            l[2 + i + 3].split(" "), 
            l[2 + i + 4].split(" ")],
        [
            [l[2 + i + c].split(" ")[0] for c in range(5)], 
            [l[2 + i + c].split(" ")[1] for c in range(5)], 
            [l[2 + i + c].split(" ")[2] for c in range(5)], 
            [l[2 + i + c].split(" ")[3] for c in range(5)], 
            [l[2 + i + c].split(" ")[4] for c in range(5)] 
        ]
    ]

checked = []
won = []

printed = False
for i in nums.split(","):
    f = False
    checked.append(i)

    for b in boards:
        for g in range(2):
            for r in range(5):
                if set(boards[b][g][r]).issubset(checked):
                    if b not in won:
                        f = True

                    # part 1

                    if not printed:
                        print("solution to part 1: {}".format(
                            int(checked[-1]) * 
                            get_unchecked_sum(boards, b)
                            )
                        )

                        printed = True
        
        if f:
            won.append(b)
            f = False

    # part 2

    if len(boards) == len(won):
        last = won[-1]

        print("solution to part 2: {}".format(
            int(checked[-1]) * 
            get_unchecked_sum(boards, last)
            )
        )
        break
