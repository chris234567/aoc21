with open("C:/Users/Chris/VSCodeProjects/AoC21/src/input/day08.txt") as f:
    l = [i.replace("\n", "") for i in f.readlines()]

# # part 1

# #len 1     4     7     8
# d = {2: 0, 4: 0, 3: 0, 7: 0}

# for i in [k.split(" | ")[1].split(" ") for k in l]:
#     for r in i:
#         if len(r) in d.keys():
#             d[len(r)] += 1

# print(sum(d.values()))

# part 2

d = [2, 4, 3, 7]
c = []


for i in [k.split(" | ")[0].split(" ") for k in l]:
    for r in i: 
        if len(r) in d:
            c.append(r)  # collect all unique nums

    m = {"a": "", "b": "", "c": "", "d": "", "e": "", "f": "", "g": ""}
    from copy import deepcopy

    while True:
        a = ["a", "b", "c", "d", "e", "f", "g"]
        for c1 in a:
            m["a"] = c1
            v = [i for i in a if i != c1]

            for c2 in v:
                m["b"] = c2
                v1 = [i for i in v if i != c2]

                for c3 in v1:
                    m["c"] = c3
                    v2 = [i for i in v1 if i != c3]

                    for c4 in v2:
                        m["d"] = c4
                        v3 = [i for i in v2 if i != c4]

                        for c5 in v3:
                            m["e"] = c5
                            v4 = [i for i in v3 if i != c5]

                            for c6 in v4:
                                m["f"] = c6
                                v5 = [i for i in v4 if i != c6]

                                for c7 in v5:
                                    m["g"] = c7
                                    
                                    fin = 0

                                    for uni in c:
                                        if len(uni) == 2:
                                            if uni[0] == m["c"] and uni[1] == m["f"]:
                                                fin += 1
                                            
                                        elif len(uni) == 3:
                                            if uni[0] == m["a"] and uni[1] == m["c"] and uni[2] == m["f"]:
                                                fin += 1

                                        elif len(uni) == 4:
                                            if uni[0] == m["b"] and uni[1] == m["c"] and uni[2] == m["d"] and uni[3] == m["f"]:
                                                fin += 1

                                        elif len(uni) == 7:
                                            if uni[0] == m["a"] and uni[1] == m["b"] and uni[2] == m["c"] and uni[3] == m["d"] and uni[4] == m["e"] and uni[5] == m["f"] and uni[6] == m["g"]:
                                                fin += 1 
                                
                                if fin == len(c):
                                    print("succesful mapping found")





                                    


# # Ansatz: erst einzigartige zahl finden > notieren
# #
# #

# n = {
#     0: "abcefg",
#     1: "cf",
#     2: "acdeg",
#     3: "acdfg",
#     4: "bcdf",
#     5: "abdfg",
#     6: "abdefg",
#     7: "acf",
#     8: "abcdefg",
#     9: "abcdfg",
# }

# d = {2: "cf", 4: "bcdf", 3: "acf", 7: "abcdefg"}
# c = {}

# m = {"a": "", "b": "", "c": "", "d": "", "e": "", "f": "", "g": ""}
# didnt_work = {"a": "", "b": "", "c": "", "d": "", "e": "", "f": "", "g": ""}

# for i in [k.split(" | ")[0].split(" ") for k in l]:
#     for r in i: 
#         if len(r) in d.keys():
#             c[r] = d[len(r)]  # collect all unique nums

#     while True:
#         fin = 0
#         didnt_work_b = False

#         for uni in c:
#             for index, char in enumerate(uni):
#                 if m.get(char) == "" or didnt_work:
#                     m[char] = uni[index]  # initial set without check

                
#         if len(uni) == 2:
#             if uni.split("") in [m["c"], m["f"]]:
#                 fin += 1
#         elif len(uni) == 3:
#             if uni.split("") in [m["a"], m["c"], m["f"]]:
#                 fin += 1
#         elif len(uni) == 4:
#             if uni.split("") in [m["b"], m["c"], m["d"], m["f"]]:
#                 fin += 1
#         elif len(uni) == 7:
#             if uni.split("") in [m["a"], m["b"], m["c"], m["d"], m["e"], m["f"], m["g"]]:
#                 fin += 1 
        
#         if fin == len(c.keys()):
#             break  # current mappings works for all unique nums




    
