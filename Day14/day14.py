def process(input):
    changes = {}
    for line in input[2:]:
        [match, add] = line.strip().split(" -> ")
        changes[match] = add
    return input[0].strip(), changes

def solve(string, changes, steps):
    from copy import deepcopy
    import numpy as np
    def insert_or_add(dict, key, value):
        try:
            dict[key] += value
        except:
            dict[key] = value
    def step(pairs, counts, changes):
        new_pairs = {}
        for pair in pairs:
            if pair in changes:
                value = pairs[pair]
                insert_or_add(new_pairs, pair[0] + changes[pair], value)
                insert_or_add(new_pairs, changes[pair] + pair[1], value)
                insert_or_add(counts, changes[pair], value)
        return new_pairs, counts
    counts, pairs = {}, {}
    for i in range(len(string)-1):
        insert_or_add(pairs, string[i] + string[i+1], 1)
        insert_or_add(counts, string[i], 1)
    insert_or_add(counts, string[len(string)-1], 1)
    new_pairs = deepcopy(pairs)
    for _ in range(steps):
        new_pairs, counts = step(new_pairs, counts, changes)
    freq = list(counts.values())
    return np.amax(freq) - np.amin(freq)

def main():
    f = open("input.txt", "r")
    string, changes = process(f.readlines())
    print(solve(string, changes, 10)) #Part 1: 5656
    print(solve(string, changes, 40)) #Part 2: 12271437788530
    f.close()

if __name__ == "__main__":
    main()