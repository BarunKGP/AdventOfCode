import re
import argparse
from pprint import PrettyPrinter

pp = PrettyPrinter()

try:
    import config
except ImportError or ModuleNotFoundError:
    import sys
    sys.path.append('/home/theleftwinger/aoc2023')
    import config



def hpalindrome(pattern):
    for i in range(1, len(pattern)):
        if pattern[i - 1] != pattern[i]:
            continue

        delta = 1
        top, bottom = i - 1, i
        rows = 1
        
        while top - delta >= 0 and bottom + delta < len(pattern):
            if pattern[top - delta] == pattern[bottom + delta]:
                rows += 1
            else:
                # print('Not a perfect match')
                rows = 0
                break

            delta += 1
        
        if rows >= 1:
            return i


def vpalindrome(pattern):
    rows, cols = len(pattern), len(pattern[0])
    pattern_T = []

    for i in range(cols):
        new_str = ""
        for j in range(rows - 1, -1, -1):
            new_str += pattern[j][i]

        pattern_T.append(new_str)
    
    # print(f'Transposed pattern: {pattern_T}')
    return hpalindrome(pattern_T)


def aoc(data):
    rows = cols = 0

    for pattern in data:
        # c = vpalindrome(pattern)
        # print(f'c={c}')
        # if c is None:
        #     r = hpalindrome(pattern)
        #     rows += r
        # else:
        #     cols += c
        r = hpalindrome(pattern)
        print(f'r={r}')
        if r is None:
            c = vpalindrome(pattern)
            cols += c
        else:
            rows += r
    print(rows, cols)
    return 100*rows + cols


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--day', '-d', type=int, required=True)
    parser.add_argument('--example', '-e', action='store_true')
    args = parser.parse_args()

    fname = 'aoc13/aoc13example.txt' if args.example else 'aoc13/aoc13data.txt'
    with open(fname, 'r') as f: 
        data = f.read()
        patterns = data.rstrip().split('\n\n')

    patterns = [p.split('\n') for p in patterns]
    # pp.pprint(patterns)
    
    # data = config.init_config(args.day, args.example)
    # print('Read data')
    #
    # print(vpalindrome(data))

    res = aoc(patterns)

    print(f'Result: {res}')


if __name__ == "__main__":
    main()

