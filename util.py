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


def flip(matrix):
    """ Flip a matrix between horizontal and vertical """
    w = len(matrix[0])
    h = len(matrix)
    return [''.join([matrix[j][i] for j in range(h)]) for i in range(w)]


def matrix_string(matrix):
    return '\n'.join([''.join(line) for line in matrix])


def intersect(line, box):
    if line[2] < box[0] or line[0] > box[2] or line[3] < box[1] or line[1] > box[3]:
        return False
    if line[0] > box[0] and line[0] < box[2]:
        if line[1] > box[1] and line[1] < box[3]:
            return True
        if line[3] > box[3]:
            return True
    if line[2] > box[0] and line[2] < box[2]:
        if line[3] > box[1] and line[3] < box[3]:
            return True
    if line[1] > box[1] and line[1] < box[3]:
        if line[2] > box[2]:
            return True
    return False
