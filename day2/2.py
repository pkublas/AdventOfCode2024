import argparse


def get_diff(report):
    indices = zip(range(0, len(report)), range(1, len(report)))
    return [report[i] - report[j] for i, j in indices]


def get_diff_in_range(report_diff):
    report_diff_in_range = [1 if 1 <= abs(e) <= 3 else 0 for e in report_diff]
    return all(report_diff_in_range)


def get_direction(report_diff):
    report_diff_above_zero = [1 if e > 0 else 0 for e in report_diff]
    report_diff_below_zero = [1 if e < 0 else 0 for e in report_diff]
    return all(report_diff_above_zero) or all(report_diff_below_zero)


def is_report_valid(report, do_recursive=True):
    report_diff = get_diff(report)
    is_diff_in_range = get_diff_in_range(report_diff)
    is_directional = get_direction(report_diff)
    report_is_valid = is_diff_in_range and is_directional
    if report_is_valid:
        return True
    elif do_recursive:
        for layer in range(0, len(report)):
            report_copy = report.copy()
            report_copy.pop(layer)
            if is_report_valid(report_copy, do_recursive=False):
                return True
        else:
            return False
    else:
        return False


def get_data(file_name, line_processor):
    with open(file_name, "r") as file:
        for line in file:
            report = [int(e) for e in line.strip().split(" ")]
            yield line_processor(report)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", type=str)
    args = parser.parse_args()
    report_status = []
    for status in get_data(file_name=args.filename, line_processor=is_report_valid):
        report_status.append(status)
    print(f"result={sum(report_status)}")
