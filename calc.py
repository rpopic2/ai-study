
symbols = []
exprs = []


def define_operator(symbol: str, expr):
    symbols.append(symbol)
    exprs.append(expr)


def calculate(input: str):
    augend, operator, addend = parse(input)
    if operator in symbols:
        i = symbols.index(operator)
        return exprs[i](augend, addend)
    else:
        print(f"Unknown operator : {operator}")


def parse(input: str):
    operator = parse_operator(input)
    front, middle, back = input.partition(operator)
    return int(front), operator, int(back)


def parse_operator(input: str):
    for x in input:
        if not x.isnumeric() and not x.isspace():
            return x


def parse_number(input: str):
    if input.isnumeric():
        return int(input)
    else:
        return None


def calc_from_cli():
    import sys
    if len(sys.argv) <= 1:
        return
    argu = ""
    sys.argv.pop(0)
    for v in sys.argv:
        argu += v
    x = calculate(argu)
    print(x)

# define_operator('+', lambda x, y: x+y)
# define_operator('-', lambda x, y: x-y)
# define_operator('*', lambda x, y: x*y)
# define_operator('/', lambda x, y: x/y)


if __name__ == "__main__":
    calc_from_cli()
