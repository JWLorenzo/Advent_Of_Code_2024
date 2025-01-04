with open("test.txt", "r") as f:
    lines = f.readlines()


def main() -> None:
    score = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "A":
                if (y >= 1 and x >= 1) and (
                    len(lines) - y > 1 and len(lines[y]) - x > 1
                ):
                    if (
                        (lines[y - 1][x - 1] == "M" and lines[y + 1][x + 1] == "S")
                        or (lines[y - 1][x - 1] == "S" and lines[y + 1][x + 1] == "M")
                    ) and (
                        (lines[y - 1][x + 1] == "M" and lines[y + 1][x - 1] == "S")
                        or (lines[y - 1][x + 1] == "S" and lines[y + 1][x - 1] == "M")
                    ):
                        score += 1

    print(score)


if __name__ == "__main__":
    main()
