import re
import argparse

try:
    import config
except ImportError or ModuleNotFoundError:
    import sys
    sys.path.append('/home/theleftwinger/aoc2023')
    import config


def parse(data):
    graph = {}
    for line in data:
        parent, nodes = line.split(' = ')
        nodes = nodes.strip('()')
        nodes = nodes.split(', ')
        graph[parent] = nodes

    return graph

def traverse(graph, instructions, head='AAA', dest='ZZZ'):
    i = 0
    count = 0
    key = head

    while key != dest:
        if key not in graph:
            print(f'Key {key} not found in graph. Returning....')
            break

        children = graph[key]
        if instructions[i] == 'L':
            key = children[0]
        else:
            key = children[1]

        i += 1
        if i == len(instructions):
             i = 0

        count += 1

    return count

# def control(graph, instructions):
#     heads = [c if c[-1] == 'A' for c in graph.keys()]


def aoc(data):
    instructions = data[0]

    graph = parse(data[2:])

    return traverse(graph, instructions)


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

