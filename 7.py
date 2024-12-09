from input_scraper import get_aoc_input
from itertools import product

def parse_input(input: str) -> list:
    equations = []
    for line in input.splitlines():
        key, values = line.split(":")
        equations.append((int(key), [int(value) for value in values.strip().split(" ")]))
    return equations

def compute_valid_equations(equations: list, operators: list) -> int:
    """
    Computes the sum of test values for equations that can be made true using +, *, and || operators.
    Operators are evaluated left-to-right, not using standard precedence rules.
    || is the concatenation operator that joins numbers (e.g., 12 || 3 = 123)
    """
    valid_equations = []
    
    for test_value, numbers in equations:
        num_operators_needed = len(numbers) - 1
        for ops in product(operators, repeat=num_operators_needed):
            result = numbers[0]
            for i, op in enumerate(ops):
                if op == '+':
                    result += numbers[i + 1]
                elif op == '*':
                    result *= numbers[i + 1]
                elif op == '||':
                    result = int(str(result) + str(numbers[i + 1]))
            
            if result == test_value:
                valid_equations.append((test_value, numbers))
                break
                
    return valid_equations

if __name__ == "__main__":
    equations = parse_input(get_aoc_input(7))
    
    # part 1
    valid_equations = compute_valid_equations(equations, ["+", "*"])
    print(sum([equation[0] for equation in valid_equations]))

    # part 2
    valid_equations = compute_valid_equations(equations, ["+", "*", "||"])
    print(sum([equation[0] for equation in valid_equations]))

