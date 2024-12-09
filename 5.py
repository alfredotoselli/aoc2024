from input_scraper import get_aoc_input 
from collections import defaultdict

def parse_input(input):
    sections = input.split("\n\n")
    rules = defaultdict(set)
    updates = []

    for line in sections[0].splitlines():
        before, after = line.split("|")
        rules[int(before)].add(int(after))
    
    for line in sections[1].splitlines():
        updates.append([int(x) for x in line.split(",")])
        
    return rules, updates

def partition_updates(rules, updates):
    correct_updates = []
    incorrect_updates = []

    for update in updates:
        saw = set()

        for page in update:
            comes_after = rules[page]
            if comes_after & saw:
                break
            saw.add(page)

        if len(saw) == len(update):
            correct_updates.append(update)
        else:
            incorrect_updates.append(update)

    return correct_updates, incorrect_updates

        
def compute_middle_sum(correct_updates):
    middle_sum = 0

    for update in correct_updates:
        m = len(update) // 2
        middle_sum += update[m]

    return middle_sum

from collections import defaultdict

def fix_updates(rules, incorrect_updates):
    def topological_sort(update):
        # Build graph
        graph = defaultdict(set)
        nodes = set(update)
        for node in nodes:
            for after in rules[node]:
                if after in nodes:
                    graph[node].add(after)

        # Find order
        result = []
        visited = set()
        temp = set()

        def visit(node):
            if node in temp:
                return  # Skip if in current path
            if node in visited:
                return  # Skip if already processed
            
            temp.add(node)
            for next_node in graph[node]:
                visit(next_node)
            temp.remove(node)
            visited.add(node)
            result.append(node)

        for node in nodes:
            if node not in visited:
                visit(node)

        return result[::-1]  # Reverse to get correct order

    return [topological_sort(update) for update in incorrect_updates]

if __name__ == "__main__":
    rules, updates = parse_input(get_aoc_input(5))

    # part 1
    correct_updates, incorrect_updates = partition_updates(rules, updates)
    middle_sum = compute_middle_sum(correct_updates)
    print(middle_sum)
    
    # part 2
    fixed_updates = fix_updates(rules, incorrect_updates)
    fixed_middle_sum = compute_middle_sum(fixed_updates)
    print(fixed_middle_sum)
