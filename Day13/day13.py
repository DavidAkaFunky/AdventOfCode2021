def process(lines):
    dots, folds = [], []
    i = 0
    while lines[i] != "\n":
        [x, y] = [int(j) for j in lines[i].strip().split(",")]
        dots.append([x, y])
        i += 1
    i += 1
    while i < len(lines):
        line = lines[i].split()
        x, y = line[2].split("=")
        folds.append([x, int(y)])
        i += 1
    return dots, folds

def solve(dots, folds, flag):
    def assign_fold(coord, dots, fold):
        for dot in dots:
            if dot[coord] > fold[1]:
                dot[coord] = 2*fold[1] - dot[coord]
    def print_sheet(dots):
        max_x, max_y = max([dot[0] for dot in dots]), max([dot[1] for dot in dots])
        sheet = [[False for _ in range(max_x + 1)] for _ in range(max_y + 1)]
        for (x, y) in dots:
            sheet[y][x] = True
        string = ""
        for y in sheet:
            for x in y:
                string += "[]" if x else "  "
            string += "\n"
        return string[:-1]
    flags = {"x": 0, "y": 1}
    for fold in folds:
        assign_fold(flags[fold[0]], dots, fold)
    dots_new = []
    [dots_new.append(x) for x in dots if x not in dots_new]
    if flag:
        return dots_new
    return print_sheet(dots_new)

def main():
    f = open("input.txt", "r")
    dots, folds = process(f.readlines())
    dots = solve(dots, [folds[0]], 1)
    print(len(dots)) #Part 1: 621
    print(solve(dots, folds[1:], 0)) #Part 2: HKUJGAJZ
    f.close()

if __name__ == "__main__":
    main()