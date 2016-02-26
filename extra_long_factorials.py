#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/extra-long-factorials

fac = n = int(input().strip())
for i in range(1, n):
    fac *= i
print(str(fac))
