import calc

calc.define_operator('+', lambda x, y: x+y)
calc.define_operator('-', lambda x, y: x-y)
calc.define_operator('*', lambda x, y: x*y)
calc.define_operator('/', lambda x, y: x/y)