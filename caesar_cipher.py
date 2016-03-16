#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/caesar-cipher-1


import string


n = int(input().strip())
s = input().strip()
k = int(input().strip())

sn = list(s)
alen = len(string.ascii_lowercase)
k %= alen
for i in range(n):
    char = s[i]
    ind = string.ascii_lowercase.find(char)
    if ind != -1:
        sn[i] = string.ascii_lowercase[(ind + k) % alen]
        continue
    ind = string.ascii_uppercase.find(char)
    if ind != -1:
        sn[i] = string.ascii_uppercase[(ind + k) % alen]
print(''.join(sn))
