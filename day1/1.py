import argparse


def get_data(file_name):
    with open(file_name, "r") as file:
        for line in file:
            _n1, _n2 = line.strip().split("   ")
            yield int(_n1), int(_n2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", type=str)
    args = parser.parse_args()
    l1, l2 = [], []
    for n1, n2 in get_data(args.filename):
        l1.append(n1)
        l2.append(n2)

    left_list = sorted(l1)
    right_list = sorted(l2)
    # print(left_list)
    # print(right_list)

    result = [abs(e1 - e2) for e1, e2 in zip(left_list, right_list)]
    # print(result)
    print(sum(result))
