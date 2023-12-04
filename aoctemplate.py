import re
import argparse

try:
    import config
except ImportError or ModuleNotFoundError:
    import sys
    sys.path.append('/home/theleftwinger/aoc2023')
    import config



def aoc(data):
    pass



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

