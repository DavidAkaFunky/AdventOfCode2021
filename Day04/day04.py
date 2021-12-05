def process(lines):
    values = [int(x) for x in lines[0].split(",")]
    cards = []
    cards_b = []
    card = []
    card_b = []
    for line in lines[2:]:
        print(line)
        if line == "\n":
            cards.append(card)
            cards_b.append(card_b)
            card = []
            card_b = []
        else:
            card.append([int(x) for x in line.split()])
            card_b.append([False for x in line.split()])
    cards.append(card)
    cards_b.append(card_b)
    return values, cards, cards_b

def check_bingo_columns(x, cards, cards_b):
        for i in range(len(cards[x][0])):
            bingo = True
            for j in range(len(cards[x])):
                if not cards_b[x][j][i]:
                    bingo = False
                    break
            if bingo:
                return True
        return False

def part1(values, cards, cards_b):
    for value in values:
        for x in range(len(cards)):
            sum = 0
            bingo = False
            for i in range(len(cards[x])):
                flag = True
                for j in range(len(cards[x][i])):
                    if cards[x][i][j] == value:
                        cards_b[x][i][j] = True
                    if not cards_b[x][i][j]:
                        sum += cards[x][i][j]
                        flag = False
                bingo = bingo or flag
            if check_bingo_columns(x, cards, cards_b) or bingo:
                return sum * value
    
def part2(values, cards, cards_b):
    wins = [False for card in cards]
    for value in values:
        for x in range(len(cards)):
            bingo = False
            for i in range(len(cards[x])):
                flag = True
                for j in range(len(cards[x][i])):
                    if cards[x][i][j] == value:
                        cards_b[x][i][j] = True
                    if not cards_b[x][i][j]:
                        flag = False
                bingo = bingo or flag
            if check_bingo_columns(x, cards, cards_b) or bingo:
                wins[x] = True
                finished = True
                for card in wins:
                    if not card:
                        finished = False
                        break
                if finished:
                    sum = 0
                    for i in range(len(cards[x])):
                        for j in range(len(cards[x][i])):
                            if not cards_b[x][i][j]:
                                sum += cards[x][i][j]
                    print(x, sum, value)
                    return sum * value

def main():
    f = open("input.txt", "r")
    values, cards, cards_b = process(f.readlines())
    print(part1(values, cards, cards_b)) #Part 1: 41503
    print(part2(values, cards, cards_b)) #Part 2: 3178
    f.close()

if __name__ == "__main__":
    main()