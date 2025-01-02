with open("test.txt", "r") as f:
    lines = f.readlines()


def main() -> None:
    safe = 0
    for report in lines:
        already_safe = False
        report = list(map(int, report.split()))

        if (report == sorted(report, reverse=True)) or (report == sorted(report)):
            for level_index in range(len(report) - 1):
                if abs(report[level_index] - report[level_index + 1]) in range(1, 4):
                    if level_index == len(report) - 2:
                        safe += 1
                        already_safe = True
                else:
                    break

        if not already_safe:
            for i in range(len(report)):
                if not already_safe:
                    if i == len(report) - 1:
                        tolerance = report[:i]
                    else:
                        tolerance = report[:i] + report[i + 1 :]

                    if (tolerance == sorted(tolerance, reverse=True)) or (
                        tolerance == sorted(tolerance)
                    ):
                        for level_index in range(len(tolerance) - 1):
                            if abs(
                                tolerance[level_index] - tolerance[level_index + 1]
                            ) in range(1, 4):
                                if level_index == len(tolerance) - 2:
                                    safe += 1
                                    already_safe = True
                            else:
                                break

    print("Safe", safe)


if __name__ == "__main__":
    main()
