def read_digits(data):
    result = ''
    digits = [str(x) for x in range(10)]
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
    digits = [str(x) for x in range(10)]
    for x in data:
        if x in digits:
            result += x
    return result

def lines_from_file(filename):
    with open(filename, 'r') as fhan:
        return fhan.readlines()
