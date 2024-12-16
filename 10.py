from input_scraper import get_aoc_input

def input_parser(input):
    return [[int(cell) for cell in line] for line in input.splitlines()]

def get_neighbors(grid, x, y):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    height = len(grid)
    width = len(grid[0])
    neighbors = []
    
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < height and 0 <= new_y < width:
            neighbors.append((new_x, new_y))
    return neighbors

def dfs(grid, x, y, visited, target_height):
    if grid[x][y] == 9:
        return {(x, y)}
    
    reachable_nines = set()
    for next_x, next_y in get_neighbors(grid, x, y):
        if (next_x, next_y) not in visited and grid[next_x][next_y] == target_height:
            visited.add((next_x, next_y))
            nines = dfs(grid, next_x, next_y, visited, target_height + 1)
            reachable_nines.update(nines)
            visited.remove((next_x, next_y))
    
    return reachable_nines

def find_trailheads_score(grid):
    height = len(grid)
    width = len(grid[0])
    total_score = 0
    
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 0:
                visited = {(i, j)}
                reachable_nines = dfs(grid, i, j, visited, 1)
                total_score += len(reachable_nines)
    
    return total_score

def dfs_count_paths(grid, x, y, visited, target_height):
    if grid[x][y] == 9:
        return 1
    
    total_paths = 0
    for next_x, next_y in get_neighbors(grid, x, y):
        if (next_x, next_y) not in visited and grid[next_x][next_y] == target_height:
            visited.add((next_x, next_y))
            paths = dfs_count_paths(grid, next_x, next_y, visited, target_height + 1)
            total_paths += paths
            visited.remove((next_x, next_y))
    
    return total_paths

def find_trailheads_rating(grid):
    height = len(grid)
    width = len(grid[0])
    total_rating = 0
    
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 0:
                visited = {(i, j)}
                paths = dfs_count_paths(grid, i, j, visited, 1)
                total_rating += paths
    
    return total_rating

if __name__ == "__main__":
    input = input_parser(get_aoc_input(10))
    result1 = find_trailheads_score(input)
    result2 = find_trailheads_rating(input)
    print(f"Part 1: {result1}")
    print(f"Part 2: {result2}")