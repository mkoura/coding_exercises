#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/alternating-characters


t = int(input().strip())
for a0 in range(t):
    l = input().strip()
    last = ''
    d = 0
    for c in l:
        if last == c:
            d += 1
        last = c
    print(str(d))
