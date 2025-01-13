import os
import sys


def load_text_file(file_path: str) -> tuple[list, list]:
    with open(
        os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), file_path), "r"
    ) as f:
        raw_rules, raw_update = f.read().split("\n\n")
        rules = [n.split("|") for n in raw_rules.split("\n")]
        updates = [n.split(",") for n in raw_update.split("\n")]

        return rules, updates


def process_rules_and_updates(rules, updates):
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
    return sum, fixed_sum


def main() -> None:
    rules, updates = load_text_file("test.txt")
    sum, fixed_sum = process_rules_and_updates(rules, updates)
    print("Sum", sum)
    print("Fixed Sum", fixed_sum)


if __name__ == "__main__":
    main()
