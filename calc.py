def calculate(input: str):
    augend, operator, addend = parse(input)

    match operator:
        case '+':
            return augend + addend
        case '-':
            return augend - addend
        case _:
            print("Unknown operator : " + operator)


def parse(input: str):
    operator = get_operator(input)
    front, middle, back = input.partition(operator)
    return int(front), operator, int(back)


def get_operator(input: str):
    for x in input:
        if not x.isnumeric() and not x.isspace():
            return x


if __name__ == "__main__":
    import sys

    argu = ""
    sys.argv.pop(0)
    for v in sys.argv:
        argu += v

    x = calculate(argu)
    print(x)
