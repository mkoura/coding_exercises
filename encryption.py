#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/encryption

import math


s = input().strip()
s.replace(" ", "")
l = len(s)
cols = int(math.ceil(math.sqrt(l)))

ccol = -1
arr = [[] for x in range(cols)]
for c in s:
    ccol += 1
    if ccol >= cols:
        ccol = 0
    arr[ccol].append(c)

final = ''
for r in arr:
    final += " " + ''.join(r)
print(final.strip())
