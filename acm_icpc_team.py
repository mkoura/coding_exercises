#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/acm-icpc-team

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
topic = []
topic_i = 0
for topic_i in range(n):
    topic_t = str(input().strip())
    topic.append(int(topic_t, 2))

mmax = mcount = 0
for i in range(n):
    t = topic.pop()
    for r in topic:
        bn = r | t
        cur = bin(bn).count('1')
        if cur > mmax:
            mmax = cur
            mcount = 1
        elif cur == mmax:
            mcount += 1
print(str(mmax))
print(str(mcount))
