def part1(input):
    h = d = 0
    for line in input:
        line = line.split()
        inst, update = line[0], int(line[1])
        if inst == "up":
            d -= update
        elif inst == "down":
            d += update
        elif inst == "forward":
            h += update
    return h * d

def part2(input):
    aim = h = d = 0
    for line in input:
        line = line.split()
        inst, update = line[0], int(line[1])
        if inst == "up":
            aim -= update
        elif inst == "down":
            aim += update
        elif inst == "forward":
            h += update
            d += aim * update
    return h * d

def main():
    f = open("input.txt", "r")
    lines = f.readlines()
    print(part1(lines)) #Part 1: 2091984
    print(part2(lines)) #Part 2: 2086261056
    f.close()

if __name__ == "__main__":
    main()