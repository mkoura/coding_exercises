#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/kaprekar-numbers

p = int(input().strip())
q = int(input().strip())

res = ''

for num in range(p, q + 1):
    nums = str(num)
    d = len(nums)
    sqrts = str(num*num)
    lsqrts = len(sqrts)
    len_ls = lsqrts - d
    if not ((len_ls == d) or (len_ls == d - 1)):
        continue
    rs = sqrts[len_ls:]
    ls = sqrts[:len_ls]
    l = int(ls) if ls != '' else 0
    r = int(rs)
    if (l + r == num):
        res += ' ' + nums
print(res.strip() if res != '' else 'INVALID RANGE')
