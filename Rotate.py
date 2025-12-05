def rotateRowRight(row):
    return [row[-1]] + row[:-1]

def rotateRowLeft(row):
    return row[1:] + [row[0]]

def rotateColDown(grid, colIndex):
    n = len(grid)
    last = grid[-1][colIndex]
    for i in range(n-1, 0, -1):
        grid[i][colIndex] = grid[i-1][colIndex]
    grid[0][colIndex] = last

def rotateColUp(grid, colIndex):
    n = len(grid)
    first = grid[0][colIndex]
    for i in range(n - 1):
        grid[i][colIndex] = grid[i + 1][colIndex]
    grid[n - 1][colIndex] = first


n, m = map(int, input("Enter grid size n and number of operations m: ").split())


grid = []
num = 1
for i in range(n):
    row = []
    for j in range(n):
        row.append(num)
        num += 1
    grid.append(row)

    print(*row, sep="\t")

for _ in range(m):
    t, k, d = input("Enter operation (t k d): ").split()
    k = int(k) - 1

    if t == 'R':
        if d == "R":
            grid[k] = rotateRowRight(grid[k])
        else:
            grid[k] = rotateRowLeft(grid[k])

    else:
        if d == "D":
            rotateColDown(grid, k)
        else:
            rotateColUp(grid, k)

for row in grid:
    print(*row, sep="\t")