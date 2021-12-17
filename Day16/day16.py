def solve(number, string, ops, flag = False, count = 0):
    from time import sleep
    i = 0
    sum = 0
    while i < len(number) - 7:
        packet_version = int(number[i : i+3], 2)
        packet_id = int(number[i+3 : i+6], 2)
        sum += packet_version
        if packet_id == 4:
            j = 6
            bits = ""
            while i+j < len(number) and int(number[i+j]) == 1:
                bits += number[i+j+1 : i+j+5]
                j += 5
            bits += number[i+j+1 : i+j+5]
            string += str(int(bits, 2)) + ","
            j += 5
        else:
            len_id = int(number[i+6])
            string += ops[packet_id]
            if len_id == 0:
                len_sub = int(number[i+7 : i+22], 2)
                (sub_sum, _, string) = solve(number[i+22 : i+22+len_sub], string, ops)
                sum += sub_sum
                j = 22 + len_sub
            elif len_id == 1:
                subpackets = int(number[i+7 : i+18], 2)
                k = 18
                for _ in range(subpackets):
                    (sub_sum, add, string) = solve(number[i+k:], string, ops, flag = True)
                    sum += sub_sum
                    k += add
                j = k
            string += "]),"
        i += j
        if flag:
            break
    return (sum, i, string)

def equal(lst):
    if len(lst) != 2:
        raise ValueError("equal" + str(len(lst)))
    return 1 if lst[0] == lst[1] else 0

def greater(lst):
    if len(lst) != 2:
        raise ValueError("greater" + str(len(lst)))
    return 1 if lst[0] > lst[1] else 0

def less(lst):
    if len(lst) != 2:
        raise ValueError("less" + str(len(lst)))
    return 1 if lst[0] < lst[1] else 0

def main():
    from numpy import product
    f = open("input.txt", "r")
    number = bin(int("1" + f.readline(), 16))[3:]
    (sum_pack, _, expr) = solve(number, "", {0: "sum([", 1: "product([", 2: "min([", 3: "max([", 5: "greater([", 6: "less([", 7: "equal(["})
    print(sum_pack) #Part 1: 860
    expr = expr[:-1]
    print(eval(expr)) #Part 2: 470949537659
    f.close()

if __name__ == "__main__":
    main()