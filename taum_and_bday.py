#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/taum-and-bday

t = int(input().strip())
for a0 in range(t):
    b, w = input().strip().split(' ')
    b, w = [int(b), int(w)]
    x, y, z = input().strip().split(' ')
    x, y, z = [int(x), int(y), int(z)]

    for_b = b * x if x <= y + z else b * (y + z)
    for_w = w * y if y <= x + z else w * (x + z)
    print(str(for_b + for_w))
