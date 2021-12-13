def process(lines):
    dots = []
    folds = []
    i = 0
    max_x = 0
    max_y = 0
    while lines[i] != "\n":
        [x, y] = [int(j) for j in lines[i].strip().split(",")]
        max_x, max_y = max(max_x, x), max(max_y, y)
        dots.append([x, y])
        i += 1
    i += 1
    while i < len(lines):
        line = lines[i].split()
        x, y = line[2].split("=")
        folds.append([x, int(y)])
        i += 1
    sheet = [[False for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for (x, y) in dots:
        sheet[y][x] = True
    return sheet, dots, folds

def solve(sheet, dots, folds, flag):
    def assign_fold(coord, dots, fold):
        for dot in dots:
            if dot[coord] > fold[1]:
                dot[coord] = 2*fold[1] - dot[coord]
                sheet[dot[1]][dot[0]] = True
    def print_sheet(sheet):
        string = ""
        for y in sheet:
            for x in y:
                string += "[]" if x else "  "
            string += "\n"
        return string
    flags = {"x": 0, "y": 1}
    for fold in folds:
        assign_fold(flags[fold[0]], dots, fold)
        if fold[0] == "y":
            sheet = sheet[:fold[1]]
        elif fold[0] == "x":
            sheet = [sheet[i][:fold[1]] for i in range(len(sheet))]
    if flag:
        count = 0
        for y in sheet:
            for x in y:
                if x:
                    count += 1
        return count
    return print_sheet(sheet)

def main():
    f = open("input.txt", "r")
    sheet, dots, folds = process(f.readlines())
    print(solve(sheet, dots, [folds[0]], 1)) #Part 1: 621
    print(solve(sheet, dots, folds[1:], 0)) #Part 2: HKUJGAJZ
    f.close()

if __name__ == "__main__":
    main()