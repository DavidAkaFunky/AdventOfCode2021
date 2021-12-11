def part1(lines):
    total = 0
    sinks = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            low = True
            value = lines[i][j]
            if i-1 >= 0:
                low = low and value < lines[i-1][j]
            if i+1 < len(lines):
                low = low and value < lines[i+1][j]
            if j-1 >= 0:
                low = low and value < lines[i][j-1]
            if j+1 < len(lines[i]):
                low = low and value < lines[i][j+1]
            if low:
                sinks.append((i,j))
                total += 1 + value
    return total, sinks

def part2(lines, sinks):
    def mark(i, j, visited, value, basin_size, lines, stack):
        if not visited[i][j] and 9 > lines[i][j] > value:
            stack.append((i, j))
            visited[i][j] = True
            return basin_size + 1
        return basin_size
    visited = [[False for _ in lines[0]] for _ in lines]
    basin_sizes = []
    for sink in sinks:
        basin_size = 1
        stack = [sink]
        while stack != []:
            (i, j) = stack.pop(-1)
            value = lines[i][j]
            if i-1 >= 0:
                basin_size = mark(i-1, j, visited, value, basin_size, lines, stack)
            if i+1 < len(lines):
                basin_size = mark(i+1, j, visited, value, basin_size, lines, stack)
            if j-1 >= 0:
                basin_size = mark(i, j-1, visited, value, basin_size, lines, stack)
            if j+1 < len(lines[i]):
                basin_size = mark(i, j+1, visited, value, basin_size, lines, stack)
        basin_sizes.append(basin_size)
    basin_sizes = sorted(basin_sizes)
    return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]

def main():
    f = open("input.txt", "r")
    input = [[int(x) for x in line.strip()] for line in f.readlines()]
    sink_number, sinks = part1(input)
    print(sink_number) #Part 1: 506
    print(part2(input, sinks)) #Part 2: 931200
    f.close()

if __name__ == "__main__":
    main()