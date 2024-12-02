import argparse


def process_line(line):
    report = [int(e) for e in line.strip().split(" ")]
    report_diff = [
        report[i] - report[j]
        for i, j in zip(range(0, len(report)), range(1, len(report)))
    ]

    report_diff_in_range = all(
        [True if 1 <= abs(e) <= 3 else False for e in report_diff]
    )
    report_diff_above_zero = all([True if e > 0 else False for e in report_diff])
    report_diff_below_zero = all([True if e < 0 else False for e in report_diff])

    return (
        1
        if report_diff_in_range and (report_diff_above_zero or report_diff_below_zero)
        else 0
    )


def get_data(file_name, line_processor):
    with open(file_name, "r") as file:
        for line in file:
            yield line_processor(line)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", type=str)
    args = parser.parse_args()
    report_status = []
    for status in get_data(file_name=args.filename, line_processor=process_line):
        report_status.append(status)
    print(f"result={sum(report_status)}")
