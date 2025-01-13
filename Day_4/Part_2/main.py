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
    return score


def main() -> None:
    lines = load_text_file("test.txt")
    score = calculate_score(lines)
    print("Score", score)


if __name__ == "__main__":
    main()
