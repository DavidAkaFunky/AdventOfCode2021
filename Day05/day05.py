def process(lines):
    max_x = max_y = 0
    res = []
    for line in lines:
        [init, end] = line.split(" -> ")
        x1, y1 = [int(x) for x in init.split(",")]
        x2, y2 = [int(x) for x in end.split(",")]
        max_x = max([x1,x2,max_x])
        max_y = max([y1,y2,max_y])
        res.append([[x1, y1],[x2, y2]])
    grid = [[0 for y in range(max_y + 1)] for x in range(max_x + 1)]
    return grid, res

def get_range(c1, c2):
    return range(c1, c2 + 1) if c1 < c2 else range(c1, c2 - 1, -1)

def hor_line(grid, x, y1, y2):
    for y in get_range(y1, y2):
        grid[x][y] += 1

def ver_line(grid, x1, x2, y):
    for x in get_range(x1, x2):
        grid[x][y] += 1

def find_overlaps(grid):
    total = 0
    for line in grid:
        for el in line:
            if el >= 2:
                total += 1
    return total

def diag_line(grid, x1, x2, y1, y2):
    for (x, y) in zip(get_range(x1, x2), get_range(y1, y2)):
        grid[x][y] += 1

def solve(grid, lines, flag):
    for [[x1, y1], [x2, y2]] in lines:
        if x1 == x2:
            hor_line(grid, x1, y1, y2)
        elif y1 == y2:
            ver_line(grid, x1, x2, y1)
        if flag and abs(x1 - x2) == abs(y1 - y2):
            diag_line(grid, x1, x2, y1, y2)
    return find_overlaps(grid)

def main():
    from copy import deepcopy
    f = open("input.txt", "r")
    grid, lines = process(f.readlines())
    print(solve(deepcopy(grid), deepcopy(lines), False)) #Part 1: 6283
    print(solve(deepcopy(grid), deepcopy(lines), True)) #Part 2: 18864
    f.close()

if __name__ == "__main__":
    main()