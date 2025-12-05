def main():
    rowsCols = int(input("Enter number of rows and columns: ").strip())

    grid = [list(map(int, list(input("Enter row {}: ".format(i + 1)).strip()))) for i in range(rowsCols)]
    numbers = set(range(1, rowsCols + 1))

    while True:
        changed = False

        for r in range(rowsCols):
            row = grid[r]
            if row.count(0) == 1:
                missingNum = list(numbers - set(row))[0]
                colIndex = row.index(0)
                grid[r][colIndex] = missingNum
                changed = True
        for c in range(rowsCols):
            col = [grid[r][c] for r in range(rowsCols)]
            if col.count(0) == 1:
                missingNum = list(numbers - set(col))[0]
                rowIndex = col.index(0)
                grid[rowIndex][c] = missingNum
                changed = True
        if not changed:
            break
    for r in range(rowsCols):
        print("".join(map(str, grid[r])))

main()