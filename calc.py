# def calculate(input):
#     augend = int(input[0])
#     addend = int(input[2])
#     return augend + addend

def calculate(input: str):
    augend, expr, addend = input.partition('+')
    return int(augend) + int(addend)


def parse_expr(input: str):
    for x in input:
        if not x.isnumeric():
            return x


if __name__ == "__main__":
    import sys
    x = calculate(sys.argv[1])
    print(x)
