#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/cavity-map

n = int(input().strip())
grid = []
grid_i = 0
for grid_i in range(n):
    grid_t = str(input().strip())
    grid.append(grid_t)

for row in range(n):
    cline = ''
    for column in range(n):
        cur = int(grid[row][column])
        if row == 0 or \
                row == (n - 1) or \
                column == 0 or \
                column == (n - 1) or \
                int(grid[row-1][column]) >= cur or \
                int(grid[row+1][column]) >= cur or \
                int(grid[row][column-1]) >= cur or \
                int(grid[row][column+1]) >= cur:
            cline += str(cur)
        else:
            cline += 'X'
    print(cline)
