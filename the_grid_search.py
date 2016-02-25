#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/the-grid-search


t = int(input().strip())
for a0 in range(t):
    R, C = input().strip().split(' ')
    R, C = [int(R), int(C)]
    G = []
    G_i = 0
    for G_i in range(R):
        G_t = str(input().strip())
        G.append(G_t)
    r, c = input().strip().split(' ')
    r, c = [int(r), int(c)]
    P = []
    P_i = 0
    for P_i in range(r):
        P_t = str(input().strip())
        P.append(P_t)

    ret = 'NO'
    found = False
    for cR in range(R):
        start = 0
        for index in iter(lambda: G[cR].find(P[0], start), -1):
            index_end = index + c
            next_R = cR + 1
            found = True
            for nr in P[1:]:
                try:
                    if nr != G[next_R][index:index_end]:
                        found = False
                        break
                    next_R += 1
                except IndexError:
                    found = False
                    break
            if found:
                break
            else:
                start = index + 1
        if found:
            ret = 'YES'
            break
    print(ret)
