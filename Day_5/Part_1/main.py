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
    return sum


def main() -> None:
    rules, updates = load_text_file("test.txt")
    sum = process_rules_and_updates(rules, updates)
    print("Sum", sum)


if __name__ == "__main__":
    main()
