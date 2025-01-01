import pprint


def main() -> None:
    d1, d2 = {}, {}
    with open("test.txt", "r") as f:
        score = 0
        for line in f:
            intlist = [str(n) for n in line.split()]
            d1[intlist[0]] = d1.get(intlist[0], 0) + 1
            d2[intlist[1]] = d2.get(intlist[1], 0) + 1

        for i in d1.keys():
            score += int(i) * d2.get(i, 0)
        print("Score", score)


if __name__ == "__main__":
    main()
