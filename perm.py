cables_info = [
    (0, 500),
    (1000, 2000),
    (2500, 3500),
    (3000, 4500),
    (3000, 5500),
    (4800, 5500),
    (5000, 7000),
    (5500, 7000),
    (7000, 9000),
    (8000, 9500),
    (5800, 7500),
    (9000, 9600)
]

starts_at = 0
ends_at = 10000


from itertools import permutations

num_cables = len(cables_info)
# num_cables = 3
walked_around = []
for picks in range(1, num_cables):

    perm_list = permutations(range(num_cables), picks)

    cables_used = []
    for case in perm_list:
        cable_usecase = []

        for i in case:
            cable_usecase.append(cables_info[i])

        cables_used.append(cable_usecase)

    print(len(cables_used))
    for usecase in cables_used:
        print(usecase)
        walked = []
        walked.append([starts_at, usecase[0][0]])
        if len(usecase) > 1:
            prev = usecase[:-1]
            curr = usecase[1:]
            for (_, off), (ride, _) in zip(prev, curr):
                walked.append([off, ride])

        walked.append([usecase[-1][-1], ends_at])

        tot_walked = 0
        for st, ed in walked:
            tot_walked += abs(ed - st)

        if tot_walked > 10000:
            continue

        walked_around.append([tot_walked, usecase])

        print('\t', tot_walked, ' | ', usecase)

    print(picks, num_cables)

print(min(walked_around, key=lambda x: x[0]))
