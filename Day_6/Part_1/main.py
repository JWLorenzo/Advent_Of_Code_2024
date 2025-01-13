import os
import sys


def load_text_file(file_path: str) -> tuple[int, int, list]:
    with open(
        os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), file_path), "r"
    ) as f:
        lines = f.read().splitlines()
        for i in range(len(lines)):
            if "^" in lines[i]:
                y = i
                for j in range(len(lines[i])):
                    if lines[i][j] == "^":
                        x = j
    return x, y, lines


def navigate_and_sum(lines, x, y, direction):
    directions_dict = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}
    arrow_dict = {0: "^", 1: ">", 2: "v", 3: "<"}
    continue_loop = True
    current_location = [x, y]
    sum = 1
    while continue_loop:
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
                current_location = [x_next, y_next]
            else:
                if direction == 3:
                    direction = 0
                else:
                    direction += 1
        else:
            continue_loop = False
    return sum


def main() -> None:
    x, y, lines = load_text_file("test.txt")
    sum = navigate_and_sum(lines, x, y, 0)
    print("Sum", sum)


if __name__ == "__main__":
    main()
