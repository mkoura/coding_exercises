#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/service-lane


n, t = input().strip().split(' ')
n, t = [int(n), int(t)]
width = [int(width_temp) for width_temp in input().strip().split(' ')]
for a0 in range(t):
    i, j = input().strip().split(' ')
    i, j = [int(i), int(j)]
    print(str(min(width[i:j+1])))
