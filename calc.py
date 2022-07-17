def calculate(input: str):
    augend, operator, addend = parse(input)

    i = symbols.index(operator)
    if i != -1:
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


if __name__ == "__main__":
    calc_from_cli()


class Operator:
    symbol = ''
    def expr(x: int, y: int): pass


# operators = []
symbols = []
exprs = []


def add_operator(op: Operator):
    operators.append(op)
    symbols.append(op.symbol)


def add_op_new(symbol: str, expr):
    symbols.append(symbol)
    exprs.append(expr)


add_op_new('+', lambda x, y: x+y)
add_op_new('-', lambda x, y: x-y)
