#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/angry-professor

t = int(input().strip())
for a0 in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ') if int(a_temp) <= 0]
    print('YES' if len(a) < k else 'NO')
