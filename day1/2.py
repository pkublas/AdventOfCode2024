import argparse
from collections import Counter, defaultdict


def get_data(file_name):
    with open(file_name, "r") as file:
        for line in file:
            _n1, _n2 = line.strip().split("   ")
            yield int(_n1), int(_n2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", type=str)
    args = parser.parse_args()
    left_list, right_list = [], []

    for n1, n2 in get_data(args.filename):
        left_list.append(n1)
        right_list.append(n2)

    right_list_counter = Counter(right_list)
    # print(right_list_counter)
    result = [e1 * right_list_counter[e1] for e1 in left_list]
    # print(result)
    print(sum(result))
