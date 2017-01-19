'''Find the minimum value to traverse a grid moving right and down.'''
def grid_min(grid):
    '''Calculate minimum path value'''
    grid = grid[:]
    next_row = grid.pop()[:]
    for i in range(len(next_row)-1, 0, -1):
        next_row[i-1] += next_row[i]
    while grid:
        row = grid.pop()[:]
        row[-1] += next_row[-1]
        for i in range(len(row)-1, 0, -1):
            row[i-1] += min(row[i], next_row[i-1])
        next_row = row
    return next_row[0]

def main():
    '''Main function for testing'''
    grid = [[1, 2, 5, 5, 5], [5, 7, 5, 5, 5], [3, 1, 1, 1, 1]]
    for row in grid:
        print(row)

    print(grid_min(grid))

if __name__ == '__main__':
    main()
