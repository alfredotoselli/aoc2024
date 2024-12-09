from input_scraper import get_aoc_input
from collections import defaultdict
from math import gcd

def parse_input(input):
    return [line for line in input.splitlines()]

def find_antinodes(antennas_map):
    freq_map = defaultdict(list)
    antinodes_positions = set()

    for i in range(len(antennas_map)):
        for j in range(len(antennas_map[0])):
            if antennas_map[i][j].isalnum():
                freq_map[antennas_map[i][j]].append((i, j))
    
    for positions in freq_map.values():
        for i in range(len(positions)):
            for j in range(i+1, len(positions)):
                row_antenna_1, col_antenna_1 = positions[i]
                row_antenna_2, col_antenna_2 = positions[j]

                row_distance = row_antenna_2 - row_antenna_1
                col_distance = col_antenna_2 - col_antenna_1

                if row_distance == 0:  # Vertical line
                    min_col = min(col_antenna_1, col_antenna_2)
                    max_col = max(col_antenna_1, col_antenna_2)
                    for col in range(0, len(antennas_map[0])):
                        if 0 <= row_antenna_1 < len(antennas_map):
                            antinodes_positions.add((row_antenna_1, col))
                
                elif col_distance == 0:  # Horizontal line
                    min_row = min(row_antenna_1, row_antenna_2)
                    max_row = max(row_antenna_1, row_antenna_2)
                    for row in range(0, len(antennas_map)):
                        if 0 <= col_antenna_1 < len(antennas_map[0]):
                            antinodes_positions.add((row, col_antenna_1))
                
                else:  # Diagonal line
                    # Calculate the slope and unit vector
                    slope = row_distance / col_distance
                    unit_row = row_distance // gcd(abs(row_distance), abs(col_distance))
                    unit_col = col_distance // gcd(abs(row_distance), abs(col_distance))
                    
                    # Add points in both directions
                    curr_row, curr_col = row_antenna_1, col_antenna_1
                    while 0 <= curr_row < len(antennas_map) and 0 <= curr_col < len(antennas_map[0]):
                        antinodes_positions.add((curr_row, curr_col))
                        curr_row -= unit_row
                        curr_col -= unit_col
                    
                    curr_row, curr_col = row_antenna_1 + unit_row, col_antenna_1 + unit_col
                    while 0 <= curr_row < len(antennas_map) and 0 <= curr_col < len(antennas_map[0]):
                        antinodes_positions.add((curr_row, curr_col))
                        curr_row += unit_row
                        curr_col += unit_col

    return antinodes_positions


if __name__ == "__main__":
    input = (get_aoc_input(8))
    antennas_map = parse_input(input)
    
    # part 1
    antinodes_positions = find_antinodes(antennas_map)
    print(len(antinodes_positions))