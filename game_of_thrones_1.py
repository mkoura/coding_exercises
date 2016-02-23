#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/game-of-thrones

line = sorted(input().strip())
lastc = ''
stat = 'YES'
count = codd = 0
for c in line:
    if lastc == c:
        count += 1
    else:
        if count % 2 != 0:
            codd += 1
            if codd > 1:
                stat = 'NO'
                break
        lastc = c
        count = 1
print(stat)
