import os
import sys


def load_text_file(file_path: str) -> list:
    with open(
        os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), file_path), "r"
    ) as f:
        return f.readlines()


def calculate_score(lines):
    score = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "X":
                if y >= 3:
                    # N
                    if (
                        lines[y - 1][x] == "M"
                        and lines[y - 2][x] == "A"
                        and lines[y - 3][x] == "S"
                    ):
                        score += 1
                    if x >= 3:
                        # NW
                        if (
                            lines[y - 1][x - 1] == "M"
                            and lines[y - 2][x - 2] == "A"
                            and lines[y - 3][x - 3] == "S"
                        ):
                            score += 1
                    if len(lines[y]) - x > 3:
                        # NE
                        if (
                            lines[y - 1][x + 1] == "M"
                            and lines[y - 2][x + 2] == "A"
                            and lines[y - 3][x + 3] == "S"
                        ):
                            score += 1
                if len(lines) - y > 3:
                    # S
                    if (
                        lines[y + 1][x] == "M"
                        and lines[y + 2][x] == "A"
                        and lines[y + 3][x] == "S"
                    ):
                        score += 1

                    if x >= 3:
                        # SW
                        if (
                            lines[y + 1][x - 1] == "M"
                            and lines[y + 2][x - 2] == "A"
                            and lines[y + 3][x - 3] == "S"
                        ):
                            score += 1
                    if len(lines[y]) - x > 3:
                        # SE
                        if (
                            lines[y + 1][x + 1] == "M"
                            and lines[y + 2][x + 2] == "A"
                            and lines[y + 3][x + 3] == "S"
                        ):
                            score += 1
                if x >= 3:
                    # W
                    if (
                        lines[y][x - 1] == "M"
                        and lines[y][x - 2] == "A"
                        and lines[y][x - 3] == "S"
                    ):
                        score += 1
                if len(lines[y]) - x > 3:
                    # E
                    if (
                        lines[y][x + 1] == "M"
                        and lines[y][x + 2] == "A"
                        and lines[y][x + 3] == "S"
                    ):
                        score += 1
    return score


def main() -> None:
    lines = load_text_file("test.txt")
    score = calculate_score(lines)
    print("Score", score)


if __name__ == "__main__":
    main()
