import re

def look(table, i, j, num):
    start_x, start_y = i - 1, j - 1
    end_x, end_y = i + 2, j + len(num) + 1

    # print()
    for x in range(start_x, end_x):
        if x < 0 or x >= len(table):
            continue
        for y in range(start_y, end_y):
            if y < 0 or y >= len(table[0]) or table[x][y].isnumeric() or table[x][y] == '.':
                # print(f'Undesirable object at {(x, y)}')
                continue
            
            return True

    return False

def find_part_idx_in_line(table, line_idx):
    if line_idx < 0 or line_idx >= len(table):
        return []

    line = table[line_idx]
    part_idxs = []

    parts = re.findall(r'\d+', line)
    for p in parts:
        if look(table, line_idx, p.start(), p.group()):
            part_idxs.append([p.start(), p.end()])

    return part_idxs


def star_look(table, i, j):
    dir = [
        [-1, 0], [0, 0], [1, 0],
        [-1, 1], [0, 1], [1, 1],
        [-1, -1], [0, -1], [1, -1],
       ]
    parts = []

    for dx, dy in dir:
        if 0 <= i + dx < len(table) and 0 <= j + dy < len(table[0]) and table[i + dx][j + dy].isnumeric():
            print(f'\nFound number containing')
            start_pos = j + dy
            while start_pos >= 0 and table[i + dx][start_pos].isnumeric():
                start_pos -= 1
            print(f'start pos = {start_pos}')
            if look(table, i + dx, start_pos + 1, table[i + dx][start_pos + 1: j + dy + 1]):
                parts.append(int(table[i + dx][start_pos + 1: j + dy + 1]))

    if len(parts) == 2:
        return parts[0] * parts[1]
    return 1


def find_part_number_idx(table, i):
    parts = []
    line = table[i]

    if i < 0 or i >= len(table):
        return parts

    for match in re.finditer(r'\d+', line):
        if look(table, i, match.start(), match.group()):
            parts.append([match.start(), match.end()])

    return parts

def is_adjacent_part(pstart, pend, sj):
    if sj in range(pstart - 1, pend + 1):
        return True
    
    return False

def is_gear(table, si, sj):
    line = table[si]
    adj_part_idxs = {}
    for i in range(-1, 2):
        adj_part_idxs[i] = find_part_number_idx(table, si + i)

    adjparts = []
    for di, parts in adj_part_idxs.items():
        # print(f'checking line {si + di}, parts = {parts}, len = {len(parts)}')
        for part_idx in parts:
            if is_adjacent_part(part_idx[0], part_idx[1], sj):
                n = table[si + di][part_idx[0]: part_idx[1]]
                adjparts.append(int(n))

    if len(adjparts) == 2:
        return adjparts[0] * adjparts[1]
    else:
        return 0
         
def main():
    table = []
    with open('aoc3data.txt', 'r') as f:
        for line in f.readlines():
            table.append(line.strip())
    
    res = 0
    for i, line in enumerate(table):
        for match in re.finditer(r'\*', line):
            res += is_gear(table, i, match.start())

    print(res)

            # parts = find_part_number_idx(table, i - 1)
            # parts.extend(find_part_number_idx(table, i + 1))
            # for part in parts:
            #     if match.start() in range(part[0] - 1, part[1] + 1)


# def main():
#     table = []
#     with open('aoc3data.txt', 'r') as f:
#         for line in f.readlines():
#             table.append(line.strip())
#     
#     res = 1
#     for i, line in enumerate(table):
#         for match in re.finditer(r'\*', line):
#             parts = find_part_number_idx(table, i - 1)
#             parts.extend(find_part_number_idx(table, i + 1))
#             for part in parts:
#                 if match.start() in range(part[0] - 1, part[1] + 1)
#
#
#         # for match in re.finditer(r'\d+', line):
#         #     num = match.group()
#         #     # print(f'match obj: {match}, num = {num}, len = {len(num)}')
#         #     if look(table, i,  match.start(), num):
#         #         # print(f'Part num: {num}')
#         #         res += int(num)
#         #
#     print(res)

if __name__ == '__main__':
    main()
