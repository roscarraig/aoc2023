digits = [str(x) for x in range(10)]

def read_digits(data):
    result = ''
    digitw = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for i in range(len(data)):
        if data[i] in digits:
            result += data[i]
        else:
            for x in digitw:
                if data[i:].startswith(x):
                    result += digitw[x]
                    continue
    return result


def extract_digits(data):
    result = ''
    for x in data:
        if x in digits:
            result += x
    return result


def lines_from_file(filename):
    with open(filename, 'r') as fhan:
        return fhan.readlines()


def issubset(small, large):
    for item in small:
        if item not in large:
            return False
        if large[item] < small[item]:
            return False
    return True


def maxdict(small, target):
    for item in small:
        if item not in target or small[item] > target[item]:
            target[item] = small[item]


def line_to_ints(line, sep=' '):
    return [int(x) for x in line.strip().split(sep)]
