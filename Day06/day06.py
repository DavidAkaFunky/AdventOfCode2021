def solve(input, days, max, respawn):
    fish = [0 for _ in range(max + 1)]
    for i in input:
        fish[i] += 1
    for _ in range(days):
        tmp = fish[0]
        for i in range(max):
            fish[i] = fish[i+1]
        fish[max] = tmp
        fish[respawn] += tmp
    total = 0
    for i in range(max + 1):
        total += fish[i]
    return total

def main():
    f = open("input.txt", "r")
    input = [int(x) for x in f.readline().split(",")]
    print(solve(input, 80, 8, 6)) #Part 1: 365862
    print(solve(input, 256, 8, 6)) #Part 2: 1653250886439
    f.close()

if __name__ == "__main__":
    main()