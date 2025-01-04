with open("test.txt", "r") as f:
    lines = f.readlines()


"""
S | # | # | S | # | # | S 
# | A | # | A | # | A | # 
# | # | M | M | M | # | # 
S | A | M | X | M | A | S 
# | # | M | M | M | # | # 
# | A | # | A | # | A | #   
S | # | # | S | # | # | S 
"""
"""
8 combinations to check

N (0,0),(1,0),(2,0),(3,0)
S (0,0),(-1,0),(-2,0),(-3,0)
E (0,0),(1,0),(2,0),(3,0)
W (0,0),(-1,0),(-2,0),(-3,0)
NE (0,0),(1,1),(2,2),(3,3)
SE (0,0),(1,-1),(2,-2),(3,-3)
NW (0,0),(-1,1),(-2,2),(-3,3)
SW (0,0),(-1,-1),(-2,-2),(-3,-3)
"""


def main() -> None:
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
    print(score)


if __name__ == "__main__":
    main()
