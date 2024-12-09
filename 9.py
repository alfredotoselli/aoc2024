from input_scraper import get_aoc_input

def input_parser(input):
    return "".join(input.splitlines())

def map_disk_blocks(disk_map):
    file_list = []
    for i in range(0, len(disk_map), 2):
        file_list.append(disk_map[i])
    
    spaces_list = []
    for i in range(1, len(disk_map), 2):
        spaces_list.append(disk_map[i])
    
    return file_list, spaces_list


def build_blocks(file_list, spaces_list):
    blocks = []

    for i, (file_block, space_block) in enumerate(zip(file_list, spaces_list)):
        for _ in range(int(file_block)):
            blocks.append(str(i))
        
        if int(space_block) > 0:
            for _ in range(int(space_block)):
                blocks.append(".")
    
    for _ in range(int(file_list[-1])):
        blocks.append(str(len(file_list) - 1))

    return blocks

def move_file_blocks(blocks):
    
    s, e = 0, len(blocks) - 1

    while s < e:
        while blocks[s] != "." and s < e:
            s += 1

        while blocks[e] == "." and s < e:
            e -= 1

        blocks[s], blocks[e] = blocks[e], blocks[s]
        s += 1
        e -= 1

    return blocks

def move_file_blocks_2(file_list, blocks):
    for file_id in range(len(file_list) - 1, -1, -1):
        file_size = int(file_list[file_id])
        
        current_start = -1
        for i in range(len(blocks)):
            if blocks[i] == str(file_id):
                current_start = i
                break
        
        best_position = -1
        consecutive_spaces = 0
        for i in range(current_start):
            if blocks[i] == ".":
                consecutive_spaces += 1
                if consecutive_spaces == file_size:
                    best_position = i - file_size + 1
                    break
            else:
                consecutive_spaces = 0
        
        if best_position != -1:
            for i in range(current_start, current_start + file_size):
                blocks[i] = "."
            
            for i in range(best_position, best_position + file_size):
                blocks[i] = str(file_id)
    
    return blocks

def compute_filesystem_checksum(blocks):
    checksum = 0
    position = 0

    for block in blocks:
        if block != ".":
            checksum += int(block) * position
        position += 1

    return checksum

if __name__ == "__main__":
    disk_map = input_parser(get_aoc_input(9))
    file_list, spaces_list = map_disk_blocks(disk_map)
    blocks = build_blocks(file_list, spaces_list)

    blocks_2 = blocks[:]
    blocks = move_file_blocks(blocks)
    checksum = compute_filesystem_checksum(blocks)
    print(checksum)

    blocks_2 = move_file_blocks_2(file_list, blocks_2)
    checksum = compute_filesystem_checksum(blocks_2)
    print(checksum)