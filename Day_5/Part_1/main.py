import pprint

with open("test.txt", "r") as f:
    raw_rules, raw_update = f.read().split("\n\n")
    rules = [n.split("|") for n in raw_rules.split("\n")]
    updates = [n.split(",") for n in raw_update.split("\n")]


def main() -> None:
    sum = 0
    rules_dict = {}
    for rule in rules:
        rules_dict[rule[0]] = rules_dict.get(rule[0], []) + [rule[1]]

    for update in updates:
        broken_update = False
        for index in range(len(update)):
            if not broken_update:
                for value in rules_dict.get(update[index], []):
                    if value in update:
                        if value in update[index:]:
                            continue
                        else:
                            broken_update = True
                            break
        if not broken_update:
            sum += int(update[len(update) // 2])
    print("Sum", sum)


if __name__ == "__main__":
    main()
