with open("test.txt", "r") as f:
    lines = f.readlines()


def main() -> None:
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
    print("Safe", safe)


if __name__ == "__main__":
    main()
