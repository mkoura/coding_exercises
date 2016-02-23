#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/chocolate-feast

t = int(input().strip())
for a0 in range(t):
    n, c, m = input().strip().split(' ')
    n, c, m = [int(n), int(c), int(m)]

    choc = int(n / c)
    n %= c
    wrap = choc
    while wrap >= m:
        fchoc = int(wrap / m)
        wrap %= m
        wrap += fchoc
        choc += fchoc

    print(choc)
