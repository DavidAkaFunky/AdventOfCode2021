def update(lines):
    def get_neighbours(lines, i, j):
        neighbours = []
        for x in range(i-1, i+2):
            if 0 <= x < len(lines):
                for y in range(j-1, j+2):
                    if 0 <= y < len(lines[i]) and (x,y) != (i,j):
                        neighbours.append((x,y))
        return neighbours
    flashes = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            lines[i][j] += 1
    flashed = [[False for _ in lines[0]] for _ in lines]
    while True:
        changed = False
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j] >= 10 and not flashed[i][j]:
                    changed = True
                    flashes += 1
                    lines[i][j] = 0
                    flashed[i][j] = True
                    for (x, y) in get_neighbours(lines, i, j):
                        if not flashed[x][y]:
                            lines[x][y] += 1
        if not changed:
            break
    return flashes

def part1(lines, limit):
    flashes = 0
    for _ in range(limit):
        flashes += update(lines)
    return flashes

def part2(lines):
    count = 0
    while True:
        count += 1
        if update(lines) == len(lines) * len(lines[0]):
            return count

def main():
    from copy import deepcopy
    f = open("input.txt", "r")
    input = [[int(x) for x in line.strip()] for line in f.readlines()]
    print(part1(deepcopy(input), 100)) #Part 1: 1613
    print(part2(deepcopy(input))) #Part 2: 510
    f.close()

if __name__ == "__main__":
    main()