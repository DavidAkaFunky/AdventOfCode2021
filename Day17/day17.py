def process(input):
    input = input.split()
    x, y = [int(i) for i in input[2][2:-1].split("..")], [int(i) for i in input[3][2:].split("..")]
    return x[0], x[1], y[0], y[1]

def find_vel_x_min(x_min):
    n = 1
    sum = 0
    while True:
        sum += n
        if sum >= x_min: #We assume it can land
            return n
        n += 1

def update_pos(x, y, vel_x, vel_y):
    return (x + vel_x, y + vel_y)

def update_vel(vel_x, vel_y):
    if vel_x > 0:
        return vel_x - 1, vel_y - 1
    elif vel_x < 0:
        return vel_x + 1, vel_y - 1
    return (vel_x, vel_y - 1)

def test(x_min, x_max, y_min, y_max, vel_x_init, vel_y_init):
    x, y, vel_x, vel_y, height = 0, 0, vel_x_init, vel_y_init, 0
    while x <= x_max and y >= y_min:
        (x, y), (vel_x, vel_y) = update_pos(x, y, vel_x, vel_y), update_vel(vel_x, vel_y)
        height = max(height, y)
        if x_min <= x <= x_max and y_min <= y <= y_max:
            print(vel_x_init, vel_y_init, height)
            return height
    return -1

def solve(x_min, x_max, y_min, y_max, vel_x_max, vel_y_max):
    height = 0
    count = 0
    for vel_x in range(find_vel_x_min(x_min), vel_x_max + 1):
        for vel_y in range(-vel_y_max, vel_y_max + 1):
            y = test(x_min, x_max, y_min, y_max, vel_x, vel_y)
            if y != -1:
                count += 1
            if y > height:
                height = y
    return height, count

def main():
    f = open("input.txt", "r")
    x_min, x_max, y_min, y_max = process(f.readline().strip())
    height, count = solve(x_min, x_max, y_min, y_max, x_max, 1000) #Brute-force with vel_y_max = 1000
    print(height) #Part 1: 30628
    print(count) #Part 2:
    f.close()

if __name__ == "__main__":
    main()