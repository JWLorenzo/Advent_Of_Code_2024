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


def count_obstructions(lines, x, y):
    directions_dict = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}
    arrow_dict = {0: "^", 1: ">", 2: "v", 3: "<"}
    obstruction_count = 0
    iteration = 0
    for y_loop in range(len(lines)):
        for x_loop in range(len(lines[y_loop])):
            loop_coords = []
            iteration += 1
            obstruct_copy = lines.copy()
            if obstruct_copy[y_loop][x_loop] not in ["^", "#"]:
                obstruct_copy[y_loop] = (
                    obstruct_copy[y_loop][:x_loop]
                    + "O"
                    + obstruct_copy[y_loop][x_loop + 1 :]
                )
                direction = 0
                continue_loop = True
                current_location = [x, y]
                while continue_loop:
                    y_next = current_location[1] + directions_dict[direction][1]
                    x_next = current_location[0] + directions_dict[direction][0]
                    if (
                        x_next >= 0
                        and x_next < len(obstruct_copy[0])
                        and y_next >= 0
                        and y_next < len(obstruct_copy)
                    ):
                        if obstruct_copy[y_next][x_next] not in ["#", "O"]:
                            obstruct_copy[y_next] = (
                                obstruct_copy[y_next][:x_next]
                                + arrow_dict[direction]
                                + obstruct_copy[y_next][x_next + 1 :]
                            )
                            obstruct_copy[current_location[1]] = (
                                obstruct_copy[current_location[1]][
                                    : current_location[0]
                                ]
                                + "X"
                                + obstruct_copy[current_location[1]][
                                    current_location[0] + 1 :
                                ]
                            )
                            current_location = [
                                x_next,
                                y_next,
                            ]
                        else:
                            if [x_next, y_next, direction] in loop_coords:
                                obstruction_count += 1
                                continue_loop = False
                                print("obstruction count", obstruction_count)

                            loop_coords.append([x_next, y_next, direction])

                            if direction == 3:
                                direction = 0
                            else:
                                direction += 1
                    else:
                        continue_loop = False
    print("obstruction count", obstruction_count)
    return obstruction_count


def main() -> None:
    x, y, lines = load_text_file("test.txt")
    obstruction_count = count_obstructions(lines, x, y)
    print("Obstruction Count", obstruction_count)


if __name__ == "__main__":
    main()
