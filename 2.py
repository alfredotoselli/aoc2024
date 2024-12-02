
from input_scraper import get_aoc_input

def parse_input(input):
    return [[int(level) for level in line.split()] for line in input.splitlines()]


def get_safe_reports(reports):
    safe_reports = 0

    for report in reports:
        is_increasing = True if report[1] > report[0] else False
        i = 1

        while i < len(report):
            if (is_increasing and report[i] < report[i - 1]) or \
                    (not is_increasing and report[i] > report[i - 1]) or \
                    report[i] == report[i - 1] or \
                    abs(report[i] - report[i - 1]) > 3:
                break
            i += 1

        if i == len(report):
            safe_reports += 1

    return safe_reports


def evaluate_report(report):
    is_increasing = True if report[1] > report[0] else False
    i = 1

    while i < len(report):
        if (is_increasing and report[i] < report[i - 1]) or \
                (not is_increasing and report[i] > report[i - 1]) or \
                report[i] == report[i - 1] or \
                abs(report[i] - report[i - 1]) > 3:
            break
        i += 1

    return i

def remove_bad_and_evaluate(report, indices):
    for index in indices:
        report_copy = report[:]
        del report_copy[index]

        i = evaluate_report(report_copy)
        if i == len(report_copy):
            return True

    return False

def get_safe_reports_2(reports):
    safe_reports = 0

    for report in reports:
        i = evaluate_report(report)
        
        if i == len(report):
            safe_reports += 1
        elif remove_bad_and_evaluate(report, [i, i - 1, i - 2]):
            safe_reports += 1

    return safe_reports

if __name__ == "__main__":
    input = get_aoc_input(2)
    reports = parse_input(input)

    # part 1
    safe_reports = get_safe_reports(reports)
    print(safe_reports)

    # part 2
    safe_reports_2 = get_safe_reports_2(reports)
    print(safe_reports_2)
