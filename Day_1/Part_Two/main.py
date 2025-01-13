import os
import sys


def load_text_file(file_path: str) -> tuple[dict, dict]:
    d1, d2 = {}, {}
    with open(
        os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), file_path), "r"
    ) as f:
        for line in f:
            intlist = [str(n) for n in line.split()]
            d1[intlist[0]] = d1.get(intlist[0], 0) + 1
            d2[intlist[1]] = d2.get(intlist[1], 0) + 1
    return d1, d2


def print_score(d1: dict, d2: dict, score) -> None:
    for i in d1.keys():
        score += int(i) * d2.get(i, 0)
    print("Score", score)


def main() -> None:
    d1, d2 = load_text_file("test.txt")
    print_score(d1, d2, 0)


if __name__ == "__main__":
    main()
