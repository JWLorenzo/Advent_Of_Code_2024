import os
import sys


def load_text_file(file_path: str) -> list:
    with open(
        os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), file_path), "r"
    ) as f:
        return f.readlines()


def process_lines(lines):
    sum_storage = 0
    do = True
    for line in lines:
        for char in range(len(line)):
            if line[char : char + 7] == "don't()" and do:
                do = False
            if line[char : char + 4] == "do()" and not do:
                do = True

            if line[char : char + 4] == "mul(" and do:
                store_int = ["", ""]
                index_to_store = 0
                for i in range(char + 4, len(line)):
                    if line[i] == "," and index_to_store == 0:
                        index_to_store += 1
                    elif line[i] == ")" and index_to_store == 1:
                        if store_int[0].isdigit() and store_int[1].isdigit():
                            sum_storage += int(store_int[0]) * int(store_int[1])
                            break
                        else:
                            break
                    elif line[i].isdigit():
                        if store_int[index_to_store] == "" and line[i] == "0":
                            pass
                        else:
                            store_int[index_to_store] += line[i]
                    else:
                        break
    return sum_storage


def main() -> None:
    sum_storage = 0
    lines = load_text_file("test.txt")
    sum_storage = process_lines(lines)
    print("Sum Storage", sum_storage)


if __name__ == "__main__":
    main()
