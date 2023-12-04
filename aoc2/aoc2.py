import re

MAX_BALLS = {
        'red': 12,
        'green': 13,
        'blue': 14,
        }

def aoc(line):
    id_slug, details = line.split(': ')
    id_num = re.search('\d+', id_slug)[0]
    
    games = details.split('; ')
    max_balls = {
        'red': 0,
        'green': 0,
        'blue': 0,
        }
    for game in games:
        balls = game.split(', ')
        for b in balls:
            # print(f'b: {b}')
            qty, color = b.split(' ')
            max_balls[color] = max(max_balls[color], int(qty))
            # if int(qty) > MAX_BALLS[color]:
            #     return 0

    # return int(id_num) 
    res = 1
    for mb in max_balls.values():
        res *= mb

    return res

def main():
    res = 0
    with open('aoc2/aoc2data.txt', 'r') as f:
        for line in f.readlines():
            res += aoc(line.strip())

    print(res)



if __name__ == "__main__":
    main()

