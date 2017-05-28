#!/usr/bin/env python3

def fibgen():
    first, second = 0, 1
    yield first
    yield second
    while True:
        first, second = second, first + second
        yield second

fb = fibgen()
for i in range(100):
    print(fb.next())
