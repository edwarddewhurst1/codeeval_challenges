size = 4

grid = [[0 for col in range(size)] for row in range(size)]

for x in range(size):
    grid[x][0] = 1
    grid[size-1][x] = 1

for x in range(size-1, -1, -1):
    for y in range(size):
        if grid[x][y] != 1:
            grid[x][y] = grid[x+1][y] + grid[x][y-1]

answer = 0

for x in range(0, size):
    for y in range(0, size):
        if x == 0:
            answer += grid[x][y]
        elif y == size-1:
            answer += grid[x][y]

answer += grid[0][size-1]
print answer
