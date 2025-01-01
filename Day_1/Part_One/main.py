def main() -> None:
    l1, l2 = [], []
    with open("test.txt", "r") as f:
        for line in f:
            intlist = [int(n) for n in line.split()]
            l1.append(intlist[0])
            l2.append(intlist[1])
    print(sum([abs(a[0] - a[1]) for a in zip(sorted(l1), sorted(l2))]))


if __name__ == "__main__":
    main()
