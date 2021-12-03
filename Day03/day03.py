def part1(lines):
    counts = [[0] * (len(lines[0])-1), [0] * (len(lines[0])-1)]
    for line in lines:
        for i in range(len(line)-1):
            counts[int(line[i])][i] += 1
    gamma = epsilon = ""
    for i in range(len(counts[0])):
        gamma += "0" if counts[0][i] > counts[1][i] else "1"
        epsilon += "1" if counts[0][i] > counts[1][i] else "0"
    return int(gamma, 2) * int(epsilon, 2)

def part2(lines):
    def recursion(lines, flag, i):
        if len(lines) == 1:
            return lines[0]
        zeros, ones = [x for x in lines if x[i] == "0"], [x for x in lines if x[i] == "1"]
        if len(ones) >= len(zeros):
            return recursion(ones if flag else zeros, flag, i+1)
        else:
            return recursion(zeros if flag else ones, flag, i+1)
    o2, co2 = recursion(lines, True, 0), recursion(lines, False, 0)
    return int(o2, 2) * int(co2, 2)

def main():
    f = open("input.txt", "r")
    lines = f.readlines()
    print(part1(lines)) #Part 1: 3242606
    print(part2(lines)) #Part 2: 4856080
    f.close()

if __name__ == "__main__":
    main()