#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/matrix-rotation-algo


M_s, N_s, R_s = input().strip().split(' ')
M, N, R = int(M_s), int(N_s), int(R_s)
matrix = []
for i in range(M):
    matrix.append(list(input().strip().split(' ')))
nestings = min((int(M / 2) + int(M % 2), int(N / 2) + int(N % 2)))

rotated_lists = []
for i in range(nestings):
    last_c = N - i - 1
    last_r = M - i - 1
    # left - right
    crow = matrix[i][i:last_c]
    # right - bottom
    for j in range(i, last_r):
        crow.append(matrix[j][last_c])
    # bottom - left
    for j in range(last_c, i, -1):
        crow.append(matrix[last_r][j])
    # left - top
    for j in range(last_r, i, -1):
        crow.append(matrix[j][i])
    rot = R % len(crow)
    rotated_lists.append(crow[rot:] + crow[:rot])

for i in range(nestings):
    last_c = N - i - 1
    last_r = M - i - 1
    n = 0
    for j in range(i, last_c):
        matrix[i][j] = rotated_lists[i][n]
        n += 1
    for j in range(i, last_r):
        matrix[j][last_c] = rotated_lists[i][n]
        n += 1
    for j in range(last_c, i, -1):
        matrix[last_r][j] = rotated_lists[i][n]
        n += 1
    for j in range(last_r, i, -1):
        matrix[j][i] = rotated_lists[i][n]
        n += 1

for i in range(M):
    print(" ".join(matrix[i]))
