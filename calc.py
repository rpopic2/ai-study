# def calculate(input):
#     augend = int(input[0])
#     addend = int(input[2])
#     return augend + addend

from curses.ascii import isspace


def calculate(input: str):
    operator = get_operator(input)
    front, middle, back = input.partition(operator)

    augend = int(front)
    addend = int(back)

    match operator:
        case '+':
            return augend + addend
        case '-':
            return augend - addend

    return int(augend) + int(addend)


def get_operator(input: str):
    for x in input:
        if not x.isnumeric() and not x.isspace():
            return x


if __name__ == "__main__":
    import sys
    x = calculate(sys.argv[1])
    print(x)
