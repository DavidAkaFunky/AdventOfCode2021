def process(lines):
    res = []
    for line in lines:
        line = line.strip().split("|")
        res.append([line[0].split(), line[1].split()])
    return res

def part1(lines, numbers):
    total = 0
    for line in lines:
        for value in line[1]:
            if len(value) in numbers:
                total += 1
    return total

def part2(lines):
    def match(sub, string):
        for x in sub:
            if x not in string:
                return False
        return True
    total = 0
    for line in lines:
        line[0] = sorted(line[0], key = len)
        for x in line[0]:
            x = sorted(x)
            if len(x) == 2:
                one = sorted(x)
            elif len(x) == 4:
                four = sorted(x)
                l = sorted([i for i in x if i not in one])
        value = ""
        for x in line[1]:
            x = sorted(x)
            lengths = {2: "1", 3: "7", 4: "4", 7: "8"}
            if len(x) in lengths:
                value += lengths[len(x)]
            elif len(x) == 5:
                if match(one, x):
                    value += "3"
                elif match(l, x):
                    value += "5"
                else:
                    value += "2"
            elif len(x) == 6:
                if match(four, x):
                    value += "9"
                elif match(l, x):
                    value += "6"
                else:
                    value += "0"
        total += int(value)
    return total

def main():
    f = open("input.txt", "r")
    input = process(f.readlines())
    print(part1(input, [2, 3, 4, 7])) #Part 1: 397
    print(part2(input)) #Part 2: 1027422
    f.close()

if __name__ == "__main__":
    main()