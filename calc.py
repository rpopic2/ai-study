# def calculate(input):
#     augend = int(input[0])
#     addend = int(input[2])
#     return augend + addend

from curses.ascii import isspace


def calculate(input: str):
    seperator = get_expr(input)
    front, middle, back = input.partition(seperator)

    augend = int(front)
    addend = int(back)

    match seperator:
        case '+':
            return augend + addend
        case '-':
            return augend - addend

    return int(augend) + int(addend)


def get_expr(input: str):
    for x in input:
        if not x.isnumeric() and not x.isspace():
            return x


if __name__ == "__main__":
    import sys
    x = calculate(sys.argv[1])
    print(x)
