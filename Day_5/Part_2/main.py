import pprint

with open("test.txt", "r") as f:
    raw_rules, raw_update = f.read().split("\n\n")
    rules = [n.split("|") for n in raw_rules.split("\n")]
    updates = [n.split(",") for n in raw_update.split("\n")]


def main() -> None:
    sum = 0
    fixed_sum = 0
    rules_dict = {}
    for rule in rules:
        rules_dict[rule[0]] = rules_dict.get(rule[0], []) + [rule[1]]

    for update in updates:
        broken = False
        for update_index in range(len(update)):
            for update_index_value in rules_dict.get(update[update_index], []):

                if update_index_value in update:
                    if update_index_value not in update[update_index:]:
                        broken = True
        if broken:
            fixed_list = [0] * len(update)
            for i in update:
                fixed_index = 0
                for j in update:
                    if i in rules_dict.get(j, []):
                        fixed_index += 1
                fixed_list[fixed_index] = i
            fixed_sum += int(fixed_list[len(fixed_list) // 2])

        else:
            sum += int(update[len(update) // 2])
    print("fixed_sum", fixed_sum)
    print("sum", sum)


if __name__ == "__main__":
    main()
