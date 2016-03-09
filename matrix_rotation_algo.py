#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/matrix-rotation-algo


M_s, N_s, R_s = input().strip().split(' ')
M, N, R = int(M_s), int(N_s), int(R_s)
matrix = []
for i in range(M):
    matrix.append(list(input().strip().split(' ')))
nestings = min((int(M / 2) + int(M % 2), int(N / 2) + int(N % 2)))

layered_matrix = []
for i in range(nestings):
    last_c = N - i - 1
    last_r = M - i - 1
    tmp = matrix[i][i:last_c]
    for j in range(i, last_r):
        tmp.append(matrix[j][last_c])
    tmp.extend(reversed(matrix[last_r][i + 1:last_c + 1]))
    for k in range(last_r, i, -1):
        tmp.append(matrix[k][i])
    layered_matrix.append(tmp)

rotated_lists = []
for m in layered_matrix:
    l = len(m)
    rot = R % l
    rotated_lists.append(m[rot:] + m[:rot])

for i in range(nestings):
    last_c = N - i - 1
    last_r = M - i - 1
    for j in range(i + 1, last_r):
        matrix[j][i] = rotated_lists[i].pop()
    for j in range(i, last_c):
        matrix[last_r][j] = rotated_lists[i].pop()
    for j in range(last_r, i, -1):
        matrix[j][last_c] = rotated_lists[i].pop()
    for j in range(last_c, i - 1, -1):
        matrix[i][j] = rotated_lists[i].pop()

for i in range(M):
    print(" ".join(matrix[i]))
