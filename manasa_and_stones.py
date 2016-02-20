#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/manasa-and-stones


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    a = int(input().strip())
    b = int(input().strip())
    mmin = min(a, b)
    mmax = max(a, b)
    dif = mmax - mmin
    min_val = mmin * (n - 1)
    max_val = mmax * (n - 1)
    if a == b:
        print(str(min_val))
    else:
        res = ''
        cur = max_val
        while cur >= min_val:
            res = str(cur) + ' ' + res
            cur -= dif
        print(res)
