
# Operators
symbols = []
exprs = []


def define_operator(symbol: str, expr):
    symbols.append(symbol)
    exprs.append(expr)


def main(input: str):
    parsed = parse(input)
    if parsed is None:
        return
    augend, operator, addend = parsed
    return calculate(augend, operator, addend)


# Calculation
def calculate(augend, operator, addend):
    if operator in symbols:
        i = symbols.index(operator)
        return exprs[i](augend, addend)
    else:
        print(f"Unknown operator : {operator}")


# parsing
def parse(input: str):
    operator = parse_operator(input)
    if operator is None:
        return
    front, middle, back = input.partition(operator)
    augend = parse_number(front)
    addend = parse_number(back)
    if augend is None or addend is None:
        return
    return parse_number(front), operator, parse_number(back)


def parse_operator(input: str):
    for x in input:
        if x in symbols:
            return x


def parse_number(input: str):
    stripped = input.strip()
    if stripped.isnumeric():
        return int(stripped)
