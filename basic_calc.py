import basic_operators
import calc
print("Calculator by rpopic2")
while 1:
    expr = input("> ")
    result = calc.calculate(expr)
    print(result)