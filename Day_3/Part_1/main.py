with open("test.txt", "r") as f:
    lines = f.readlines()


def main() -> None:
    sum_storage = 0
    for line in lines:
        # print(line)
        for char in range(len(line)):
            if line[char : char + 4] == "mul(":
                store_int = ["", ""]
                index_to_store = 0
                for i in range(char + 4, len(line)):
                    if line[i] == "," and index_to_store == 0:
                        index_to_store += 1
                    elif line[i] == ")" and index_to_store == 1:
                        print(store_int)
                        if store_int[0].isdigit() and store_int[1].isdigit():
                            sum_storage += int(store_int[0]) * int(store_int[1])
                            print(store_int)
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
    print(sum_storage)


if __name__ == "__main__":
    main()
