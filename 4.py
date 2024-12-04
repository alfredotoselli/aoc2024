from collections import defaultdict
from input_scraper import get_aoc_input

def parse_input(input):
    return [[cell for cell in row] for row in input.splitlines()]

def _search_word(dir, grid, i, j):
    word = "MAS"
    found = 0

    for k in range(len(word)):
        i += dir[0]
        j += dir[1]
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) \
            and word[k] == grid[i][j]:

            found += 1
    
    return 1 if found == len(word) else 0

def xmas_occurrences(grid):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]
    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "X":
                for dir in dirs:
                    count += _search_word(dir, grid, i, j)                                

    return count

def _search_word_2(dir, grid, i, j):
    word = "AS"

    a_cord = ()
    found = 0
    for k in range(len(word)):
        i += dir[0]
        j += dir[1]
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) \
            and word[k] == grid[i][j]:

            found += 1
            if word[k] == "A":
                a_cord = (i, j)

    return a_cord if found == len(word) else None

def x_mas_occurrences(grid):
    """
    The idea is to find diagonal occurrences of "MAS" and then overlapping "A" two by two.
    """
    dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    a_cords = defaultdict(int)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "M":
                for dir in dirs:
                    a_cord = _search_word_2(dir, grid, i, j)
                    if a_cord:
                        a_cords[a_cord] += 1

    a_pair_count = 0
    for count in a_cords.values():
        if count == 2:
            a_pair_count += 1

    return a_pair_count


if __name__ == "__main__":
    grid = parse_input(get_aoc_input(4))  
    
    # part 1
    count = xmas_occurrences(grid)
    print(count)

    # part 2
    count_2 = x_mas_occurrences(grid)
    print(count_2)
    
