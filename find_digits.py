#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/find-digits

t = int(input().strip())
for a0 in range(t):
    num = int(input().strip())
    l = list(str(num))
    c = 0
    for i in l:
        n = int(i)
        if (n > 0 and num % n == 0):
            c += 1
    print(str(c))
