import re
from pprint import PrettyPrinter
import argparse


try:
    import config
except ImportError or ModuleNotFoundError:
    import sys
    sys.path.append('/home/theleftwinger/aoc2023')
    import config

pp = PrettyPrinter(width=30, indent=4)

class Seed:
    def __init__(self, num):
        self.seed = num
        self.var_name = 'self'
        self.var_value = num
        self.location = None

    def set_var(self, var, value):
        assert var in ['soil', 'fertilizer', 'water', 'humidity', 'light', 'temperature', 'location'],\
            f"incorrect variable {var}"
        if var == 'location':
            self.location = value
            return

        self.var_name = var
        self.var_value = value

    def get_var(self):
        return self.var_name, self.var_value


# def build_map(lines, header):
#     header_slug, _ = header.split(' ')
#     src, _, dest = header_slug.split('-')
#
#     mapping = {}
#
#     for line in lines:
#         dest_start, src_start, count = [int(w) for w in line.split(' ')]
#         # print(f'src={src_start}, dest={dest_start}, range={count}')
#         for i in range(count):
#             mapping[src_start + i] = dest_start + i
#
#     return mapping, dest
#
# def update_seeds(seeds, mapping, var):
#     new_seeds = []
#     for seed in seeds:
#         seed.set_var(var, mapping.get(seed.var_value, seed.var_value))
#         new_seeds.append(seed)
#
#     return new_seeds


def update_seeds(seeds, block, varname):
    for s in seeds:
        updated = False
        for line in block:
            dest, src, count = [int(n) for n in line.split(' ')]
            if 0 <= (s.var_value - src) < count:
                s.set_var(varname, dest + s.var_value - src)
                updated = True
                break
        
        # No match found in block
        # Rewrite same value
        if not updated:
            s.set_var(varname, s.var_value)
        

def find_min_location(seeds):
    res = float('inf')
    for s in seeds:
        res = min(res, s.location)

    return res


def aoc(data):
    seed_nums = re.findall(r'\d+', data[0].split(': ')[1])
    seeds = [Seed(int(s)) for s in seed_nums]
    
    i = 2
    while i < len(data):
        line = data[i]
        i += 1
        
        if len(line) == 0:
            continue
        
        if line[-1] == ':':
            header, _ = line.split(' ')
            src, _, dest = header.split('-')
            
            block = []
            while i < len(data) and data[i] != '':
                block.append(data[i])
                i += 1
                
            update_seeds(seeds, block, dest)
            
    return find_min_location(seeds)


    # res = None
    # i = 0
    # seeds = []
    # while i < len(data):
    #     line = data[i]
    #
    #     if i == 0:
    #         seeds = re.findall(r'\d+', line)
    #         print(f'seed numbers = {seeds}')
    #         seeds = [Seed(int(s)) for s in seeds]
    #         i += 1
    #         continue
    #     
    #     if len(line) == 0:
    #         i += 1
    #         continue
    #
    #     if line[-1] == ':':
    #         header = line
    #         map_details = []
    #         i += 1
    #         while i < len(data) and data[i] != '':
    #             map_details.append(data[i])
    #             i += 1
    #
    #         mapping, dest = build_map(map_details, header)
    #         seeds = update_seeds(seeds, mapping, dest)
    #
    #     i += 1
    #
    #
    # res = float('inf')
    # for s in seeds:
    #     res = min(res, s.location)
    #
    # return res

def _debug_seeds(seeds, end_newline=True):
    for s in seeds:
        if s.location:
            print(f'Seed({s.seed}) [location = {s.location}]')
        else:
            print(f'Seed({s.seed}) [{s.var_name} = {s.var_value}]')
    
    if end_newline:
        print()
    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--day', '-d', type=int, required=True)
    parser.add_argument('--example', '-e', action='store_true')
    args = parser.parse_args()
    
    data = config.init_config(args.day, args.example)
    print('Read data')
    # print('data:', data)

    res = aoc(data)

    print(f'Result: {res}')
 

if __name__ == "__main__":
    main()

