import re

def calibrate_line(line):
    digitWords = {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9',
    }
    choi = []
    
    for i, ch in enumerate(line):
        if ch.isnumeric():
            choi.append(ch)
        
        else:
            for word in digitWords:
                if i + len(word) - 1 < len(line) and \
                        line[i: i + len(word)] == word:
                            choi.append(word)
    
    # Convert words to digits
    for i, ch in enumerate(choi):
        if ch in digitWords:
            choi[i] = digitWords[ch]


    return choi




def find_calibration(line):
    
    choi = calibrate_line(line)
    choi_res = ''
    if len(choi) == 0:
        choi_res = '0'
    else:
        choi_res = choi[0] + choi[-1]


    # pattern = '\d|one|two|three|four|five|six|seven|eight|nine'
    pattern = r'(?:zero|one|two|three|four|five|six|seven|eight|nine|\d)'
    matches = re.findall(pattern, line)
    # print(matches)


    digitWords = {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9',
    }

    # digits = [s for s in line if (s.isnumeric() or s in digitWords)]
    regex_res = ''
    if len(matches) == 0:
        # print(f'{line} -> no matches')
        regex_res = '0'
        # return 0 
    else:
        regex_res = digitWords.get(matches[0], matches[0]) + \
            digitWords.get(matches[-1], matches[-1])
 
    if regex_res != choi_res:
        print(f'Mismatch in {line}: re -> {regex_res}, ch -> {choi_res}')

    return choi_res

    # if len(digits) == 0:
    #    return 0
    
    # return digitWords.get(digits[0], digits[0]) + \
    #         digitWords.get(digits[-1], digits[-1])


    # return digitWords.get(matches[0], matches[0]) + \
            # digitWords.get(matches[-1], matches[-1])


def main():
    res = 0
    with open('aoc1data-1.txt', 'r') as f:
        for line in f.readlines():
            num = find_calibration(line) 
            # print(f'line = {line}, num = {num}')
            res += int(num)


    print(res)


if __name__ == "__main__":
    main()
