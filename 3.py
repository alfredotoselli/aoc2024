from input_scraper import get_aoc_input
import re

def parse_input(input):
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    muls = re.findall(pattern, input)

    factors = [ mul.split("(")[1].split(")")[0].split(",") for mul in muls]
    return factors

def parse_input_2(input):
    pattern = r'don\'t\(\)|do\(\)|mul\(\d{1,3},\d{1,3}\)'
    instructions = re.findall(pattern, input)

    factors = []
    do = True
    for i in instructions:
        if i == "don't()":
            do = False
        elif i == "do()":
            do = True

        if do:
            if i.startswith("mul"):
                factors.append(i.split("(")[1].split(")")[0].split(","))

    return factors

def compute_mul(factors):
    tot = 0
    for f in factors:
        tot += int(f[0]) * int(f[1])
    return tot

if __name__ == "__main__":
    # part 1
    factors = parse_input(get_aoc_input(3))  
    total = compute_mul(factors)
    print(total)

    # part 2
    factors = parse_input_2(get_aoc_input(3))  
    total = compute_mul(factors)
    print(total)
