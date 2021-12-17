def solve(number):
    from time import sleep
    i = 0
    sum = 0
    while i < len(number) - 7:
        packet_version = int(number[i : i+3], 2)
        packet_id = int(number[i+3 : i+6], 2)
        sum += packet_version
        if packet_id == 4:
            j = 6
            while i+j < len(number) and int(number[i+j]) == 1:
                j += 5
            j += 5
        else:
            len_id = int(number[i+6])
            if len_id == 0:
                len_sub = int(number[i+7 : i+22], 2)
                sum += solve(number[i+22 : i+22+len_sub])[0]
                j = 22 + len_sub
            elif len_id == 1:
                subpackets = int(number[i+7 : i+18], 2)
                k = 0
                for l in range(subpackets):
                    (sub_sum, add) = solve(number[i+k+18:])
                    sum += sub_sum
                    k += add
                j = 25 + k
        i += j
    return (sum, i)

def main():
    f = open("input.txt", "r")
    number = bin(int("1" + f.readline(), 16))[3:]
    (sum, _) = solve(number)
    print(sum) #Part 1: 860
    #print(total) #Part 2: ???
    f.close()

if __name__ == "__main__":
    main()