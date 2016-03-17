#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/sherlock-and-squares


import math


t = int(input().strip())
for a0 in range(t):
    a, b = input().strip().split(' ')
    a, b = int(a), int(b)

    print(str(int(math.floor(math.sqrt(b))) - int(math.ceil(math.sqrt(a))) + 1))
