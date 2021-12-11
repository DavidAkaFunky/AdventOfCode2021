def part1(input, openers, closers):
    from copy import deepcopy
    matches = {"(": ")", "[": "]", "{": "}", "<": ">"}
    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
    total = 0
    correct = [True for _ in input]
    for i in range(len(input)):
        stack = []
        for symbol in input[i]:
            if symbol in openers:
                stack.append(symbol)
            elif symbol in closers:
                if symbol == matches[stack[-1]]:
                    stack.pop(-1)
                else:
                    total += scores[symbol]
                    correct[i] = False #Find the correct lines
                    break
    filtered = [input[i] for i in range(len(input)) if correct[i]]
    return filtered, total

def part2(input, openers, closers):
    points = {"(": 1, "[": 2, "{": 3, "<": 4}
    scores = []
    for line in input:
        stack = []
        score = 0
        for symbol in line:
            if symbol in openers:
                stack.append(symbol)
            elif symbol in closers: #Assuming there's always a match (the lines have been filtered)
                stack.pop(-1)
        for el in stack[::-1]:
            score *= 5
            score += points[el]
        scores.append(score)   
    return sorted(scores)[len(scores)//2]

def main():
    f = open("input.txt", "r")
    input = f.readlines()
    openers = ["(", "[", "{", "<"]
    closers = [")", "]", "}", ">"]
    filtered, total = part1(input, openers, closers)
    print(total) #Part 1: 315693
    print(part2(filtered, openers, closers)) #Part 2: 7106733059503901983453641336555852427667070276273514968500695283628709950375452011609398430944295055148883184854397404039618692837678007231383723292919025906001522038718298468500833759515017837619723558720292576907909096665629510305341637479614463089939364263523858251590926665919073299835521216914351036482602316269053294934131196715090222738943927617720894191266792444885132737724850053287518052241423095745136281708877103932560409
    f.close()

if __name__ == "__main__":
    main()