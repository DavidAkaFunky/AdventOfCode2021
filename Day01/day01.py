def solve(x, k):
    count = 0
    for i in range(k,len(x)):
        if x[i] > x[i-k]:
            count += 1
    return count

def main():
    f = open("input.txt", "r")
    print(f.readlines())
    input = [int(x) for x in f.readlines()]
    print(solve(input, 1)) #Part 1: 1548
    print(solve(input, 3)) #Part 2: 1589
    f.close()

if __name__ == "__main__":
    main()