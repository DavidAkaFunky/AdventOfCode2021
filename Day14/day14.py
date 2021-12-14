def process(input):
    changes = {}
    for line in input[2:]:
        [match, add] = line.strip().split(" -> ")
        changes[match] = add
    return input[0].strip(), changes

def solve(string, changes, steps):
    from copy import deepcopy
    import numpy as np
    def step(pairs, counts, changes):
        new_pairs = {}
        for pair in pairs:
            if pair in changes:
                value = pairs[pair]
                try:
                    new_pairs[pair[0] + changes[pair]] += value
                except KeyError:
                    new_pairs[pair[0] + changes[pair]] = value
                try:
                    new_pairs[changes[pair] + pair[1]] += value
                except KeyError:
                    new_pairs[changes[pair] + pair[1]] = value
                try:
                    counts[changes[pair]] += value
                except KeyError:
                    counts[changes[pair]] = value
        return new_pairs, counts
    counts, pairs = {}, {}
    for i in range(len(string)-1):
        try: 
            pairs[string[i] + string[i+1]] += 1
        except KeyError:
            pairs[string[i] + string[i+1]] = 1
        try:
            counts[string[i]] += 1
        except KeyError:
            counts[string[i]] = 1
    try: 
        counts[string[len(string)-1]] += 1
    except KeyError:
        counts[string[len(string)-1]] = 1 
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