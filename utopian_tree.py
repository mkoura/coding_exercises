#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/utopian-tree

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    p = int(n / 2)
    s = 1 if n % 2 == 0 else 2
    print(2**(p+s) - s)
