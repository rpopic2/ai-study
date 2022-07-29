import basic_operators
import calc

version = 0.2

print(f"Calculator {version} by rpopic2 | ? for help")
while 1:
    try:
        expr = input("> ")
    except (EOFError, KeyboardInterrupt):
        exit()
    print(calc.main_loop(expr))
