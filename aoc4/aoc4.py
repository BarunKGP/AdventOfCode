import re
import argparse

try:
    import config
except ImportError or ModuleNotFoundError:
    import sys
    sys.path.append('/home/theleftwinger/aoc2023')
    import config



def parse_line(line):
    _, nums = line.split(': ')
    winning, have = nums.split(' | ')
    winning = re.findall(r'\d+', winning)
    have = re.findall(r'\d+', have)

    return winning, have

def get_score(win, own):
    matches = set(win).intersection(set(own))

    return 2 ** (len(matches) - 1) if len(matches) > 0 else 0
    

def aoc(data):
    score = 0
    for i, line in enumerate(data):
        winning, have = parse_line(line)
        s = get_score(winning, have)
        # print(f'Score for line {i + 1} = {s}')
        score += s

    return score       



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--day', '-d', type=int, required=True)
    parser.add_argument('--example', '-e', action='store_true')
    args = parser.parse_args()
    
    data = config.init_config(args.day, args.example)
    print('Read data')

    res = aoc(data)

    print(f'Result: {res}')
 

if __name__ == "__main__":
    main()

