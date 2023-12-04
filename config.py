import os

def get_day(day, example=False):
    path = f'./aoc{day}/aoc{day}{"data" if not example else "example"}.txt'
    print(path)
    data = []
    with open(path, 'r') as f:
        for line in f.readlines():
            data.append(line.strip())

    print(type(data))
    print(len(data))

    return data

def init_config(day, example=False):
    return get_day(day, example)
