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
    return parse_number(front), operator, parse_number(back)


def parse_operator(input: str):
    for x in input:
        if not x.isnumeric() and not x.isspace():
            return x


def parse_number(input: str):
    stripped = input.strip()
    if stripped.isnumeric():
        return int(stripped)
    else:
        return 0
