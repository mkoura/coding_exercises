#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/funny-string


t = int(input().strip())
for a0 in range(t):
    S = input().strip()
    l = len(S)
    end = l - 2
    for begin in range(1, l):
        if abs(ord(S[begin]) - ord(S[begin - 1])) != abs(ord(S[end]) - ord(S[end + 1])):
            print("Not Funny")
            break
        end -= 1
    else:
        print("Funny")
