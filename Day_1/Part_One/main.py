import os
import sys


def load_text_file(file_path: str) -> tuple[list, list]:
    l1, l2 = [], []
    with open(
        os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), file_path), "r"
    ) as f:
        for line in f:
            intlist = [int(n) for n in line.split()]
            l1.append(intlist[0])
            l2.append(intlist[1])
    return l1, l2


def print_sum(l1: list, l2: list) -> None:
    print(sum([abs(a[0] - a[1]) for a in zip(sorted(l1), sorted(l2))]))


def main() -> None:
    l1, l2 = load_text_file("test.txt")
    print_sum(l1, l2)


if __name__ == "__main__":
    main()
