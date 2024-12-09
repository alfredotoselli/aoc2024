from input_scraper import get_aoc_input

def parse_input(input):
    return [[cell for cell in list(line)] for line in input.splitlines()]

def find_starting_position(input):
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == "^":
                return (i, j)

def turn_right_90_degrees(direction):
    if direction == (-1, 0):
        return (0, 1)
    elif direction == (0, 1):
        return (1, 0)
    elif direction == (1, 0):
        return (0, -1)
    else:
        return (-1, 0)

def compute_guard_path(grid, start_coord):

    path_coords = set(start_coord)
    current_coord = start_coord
    
    row, col = current_coord[0], current_coord[1]
    direction = (-1, 0)
    while 0 < row < len(grid) - 1 and 0 < col < len(grid[row]) - 1:

        # assumes there is a valid path
        while grid[row + direction[0]][col + direction[1]] == "#":
            direction = turn_right_90_degrees(direction)
        
        row += direction[0]
        col += direction[1]
        current_coord = (row, col)
        path_coords.add(current_coord)

    return path_coords

def is_loop_forming_position(grid, start_coord, obstacle_pos):
    test_grid = [row[:] for row in grid]
    if obstacle_pos == start_coord:
        return False
    test_grid[obstacle_pos[0]][obstacle_pos[1]] = "#"
    
    visited = set()
    current = start_coord
    direction = (-1, 0)
    
    while True:
        row, col = current
        # Check if we're at the boundary
        if not (0 < row < len(test_grid) - 1 and 0 < col < len(test_grid[row]) - 1):
            return False
            
        state = (current, direction)
        if state in visited:
            return True
        visited.add(state)
        
        # Check if blocked and turn right if needed
        while test_grid[row + direction[0]][col + direction[1]] == "#":
            direction = turn_right_90_degrees(direction)
            
        # Move forward
        row += direction[0]
        col += direction[1]
        current = (row, col)

def find_all_loop_positions(grid, start_coord):
    loop_positions = set()
    
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            if grid[i][j] != "#" and (i, j) != start_coord:
                if is_loop_forming_position(grid, start_coord, (i, j)):
                    loop_positions.add((i, j))
    
    return loop_positions

if __name__ == "__main__":
    input = parse_input(get_aoc_input(6))

    # part 1
    start_coord = find_starting_position(input)
    path_coords = compute_guard_path(input, start_coord)
    print(len(path_coords))

    # part 2
    loop_positions = find_all_loop_positions(input, start_coord)
    print(len(loop_positions))
    

