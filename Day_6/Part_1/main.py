with open("test.txt", "r") as f:
    lines = f.read().splitlines()
    for i in range(len(lines)):
        if "^" in lines[i]:
            y = i
            for j in range(len(lines[i])):
                if lines[i][j] == "^":
                    x = j


def main() -> None:
    direction = 0
    """
    0 = North
    1 = East
    2 = South
    3 = West
    """
    directions_dict = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}
    arrow_dict = {0: "^", 1: ">", 2: "v", 3: "<"}
    countinue_loop = True
    current_location = [x, y]
    sum = 1
    while countinue_loop:
        y_next = current_location[1] + directions_dict[direction][1]
        x_next = current_location[0] + directions_dict[direction][0]
        if (
            x_next >= 0
            and x_next < len(lines[0])
            and y_next >= 0
            and y_next < len(lines)
        ):
            if lines[y_next][x_next] == ".":
                sum += 1
            if lines[y_next][x_next] != "#":
                lines[y_next] = (
                    lines[y_next][:x_next]
                    + arrow_dict[direction]
                    + lines[y_next][x_next + 1 :]
                )
                lines[current_location[1]] = (
                    lines[current_location[1]][: current_location[0]]
                    + "X"
                    + lines[current_location[1]][current_location[0] + 1 :]
                )
                current_location = [
                    x_next,
                    y_next,
                ]
            else:
                if direction == 3:
                    direction = 0
                else:
                    direction += 1
        else:
            countinue_loop = False
            for line in lines:
                print(line)
            print("sum", sum)


if __name__ == "__main__":
    main()
