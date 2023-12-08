import re
import argparse
from collections import Counter
from functools import cmp_to_key

try:
    import config
except ImportError or ModuleNotFoundError:
    import sys
    sys.path.append('/home/theleftwinger/aoc2023')
    import config


def parse(data):
    cards = []
    bids = []
    for line in data:
        c, b = line.split(' ')
        cards.append(c)
        bids.append(int(b))

    return cards, bids

def get_type(card):
    assert len(card) == 5, f"invalid hand, len = {len(card)}"
    
    count = Counter(card)
    value_of = {
        'FIVE_OF_A_KIND': 1,
        'FOUR_OF_A_KIND': 2,
        'FULL_HOUSE': 3,
        'THREE_OF_A_KIND': 4,
        'TWO_PAIR': 5,
        'ONE_PAIR': 6,        
        'HIGH_CARD': 7,
    }

    if len(count) == 1:
        return value_of['FIVE_OF_A_KIND']

    elif len(count) == 2:
        if max(count.values()) == 4:
            return value_of['FOUR_OF_A_KIND']
        else:
            return value_of['FULL_HOUSE']

    elif len(count) == 3:
        if max(count.values()) == 3:
            return value_of['THREE_OF_A_KIND']
        else:
            return value_of['TWO_PAIR']

    elif len(count) == 4:
        return value_of['ONE_PAIR']

    else:
        return value_of['HIGH_CARD']

def compare_same_type(c1, c2):
    values_of = {c: i for i, c in enumerate('23456789TJQKA')}
    for a, b in zip(c1, c2):
        if values_of[a] == values_of[b]:
            continue
        elif values_of[a] < values_of[b]:
            return -1
        else:
            return 1
    return 0


def compare_cards(c1, c2):
    if get_type(c1) < get_type(c2):
        return 1
    elif get_type(c1) > get_type(c2):
        return -1
    else:
        return compare_same_type(c1, c2)




def sort_cards(cards):
    ranks = [get_type(c) for c in cards]  
    sorted_cards = [c for _, c in sorted(zip(ranks, cards))]
    return sorted_cards




def aoc(data):
    cards, bids = parse(data)
    sorted_cards = sorted(cards, key=cmp_to_key(compare_cards))

    rank = {}
    for i, c in enumerate(sorted_cards):
        if c in rank:
            print(f'{c} is already ranked with rank {rank[c]}')
        rank[c] = i + 1

    res = 0
    for i, c in enumerate(cards):
        # print(f'{bids[i]} * {rank[c]}')
        res += rank[c] * bids[i]

    return res



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

