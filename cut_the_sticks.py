#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/cut-the-sticks

n = int(input().strip())
arr = sorted([int(arr_temp) for arr_temp in input().strip().split(' ')], reverse=True)
length = n
for c in range(n):
    print(str(length))
    try:
        cut = arr.pop()
        while True:
            tcut = arr.pop()
            if tcut != cut:
                arr.append(tcut)
                break
    except IndexError:
        break

    length = 0
    for n in arr:
        n -= cut
        length += 1
