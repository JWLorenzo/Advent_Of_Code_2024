import os
import sys


def load_text_file(file_path: str) -> list:
    with open(
        os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), file_path), "r"
    ) as f:
        return f.readlines()


def check_reports(lines):
    safe = 0
    for report in lines:
        report = list(map(int, report.split()))

        if (report == sorted(report, reverse=True)) or (report == sorted(report)):
            for level_index in range(len(report) - 1):
                if abs(report[level_index] - report[level_index + 1]) in range(1, 4):
                    if level_index == len(report) - 2:
                        safe += 1
                else:
                    break
    return safe


def main() -> None:
    safe = 0
    lines = load_text_file("test.txt")
    safe = check_reports(lines)
    print("Safe", safe)


if __name__ == "__main__":
    main()
