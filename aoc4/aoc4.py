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
    
    # Part 1      
    # return 2 ** (len(matches) - 1) if len(matches) > 0 else 0

   # Part 2 
    return len(matches)
    

def aoc(data):
    # score = 0
    score = {i: 1 for i in range(1, len(data) + 1)}
    for i, line in enumerate(data):
        winning, have = parse_line(line)
        s = get_score(winning, have)
        for x in range(1, s + 1):
            score[i + x + 1] += score[i + 1] 

        # print(f'Score for line {i + 1} = {s}')
        # score += s 

    return sum(score.values())



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

