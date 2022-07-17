import basic_operators
import calc

version = 0.1

print(f"Calculator {version} by rpopic2")
while 1:
    expr = input("> ")
    if expr == "exit":
        exit()
    result = calc.calculate(expr)
    print(result)
