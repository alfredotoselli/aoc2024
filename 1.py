from input_scraper import get_aoc_input
from collections import Counter

def parse_input(input):
    left_list = []
    right_list = []
    for line in input.splitlines():
        x, y = line.split()
        left_list.append(int(x))
        right_list.append(int(y))
    
    return left_list, right_list

def find_distances(left_list, right_list):
    total_distance = 0

    left_list.sort()
    right_list.sort()
    for left, right in zip(left_list, right_list):
        total_distance += abs(left - right)

    return total_distance

def similarity_score(left_list, right_list):
    
    similarity_score = 0
    frequency = Counter(right_list)
    for left in left_list:
        similarity_score += left * frequency[left]
    
    return similarity_score


if __name__ == "__main__":
    input = get_aoc_input(1)
    left_list, right_list = parse_input(input)

    # part 1
    total_distance = find_distances(left_list, right_list)
    # part 2
    score = similarity_score(left_list, right_list)

    print(total_distance)
    print(score)
