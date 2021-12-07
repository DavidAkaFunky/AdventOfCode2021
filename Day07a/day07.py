def solve(input, flag):
    import numpy as np
    input = np.array(input)
    fuels = []
    for x in range(np.max(input) + 1):
        if flag:
            fuel = np.sum([abs(crab - x)*(abs(crab - x) + 1)//2 for crab in input])
        else:
            fuel = np.sum([abs(crab - x) for crab in input])
        fuels.append(fuel)
    return min(fuels)


def main():
    f = open("input.txt", "r")
    input = [int(x) for x in f.readline().split(",")]
    print(solve(input, False)) #Part 1: 355989
    print(solve(input, True)) #Part 2: 102245489
    f.close()

if __name__ == "__main__":
    main()