#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/pangrams

import string


s = input().strip().lower()
ss = ''.join(sorted(set(s))).strip()
print('pangram' if ss == string.ascii_lowercase else 'not pangram')
