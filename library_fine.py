#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/library-fine

d1, m1, y1 = input().strip().split(' ')
d1, m1, y1 = [int(d1), int(m1), int(y1)]
d2, m2, y2 = input().strip().split(' ')
d2, m2, y2 = [int(d2), int(m2), int(y2)]

fine = 0
ly = y1 - y2
lm = m1 - m2
ld = d1 - d2
if ly > 0:
    fine = 10000
elif ly < 0:
    pass
elif lm > 0:
    fine = 500 * lm
elif lm < 0:
    pass
elif ld > 0:
    fine = 15 * ld

print(str(fine))
