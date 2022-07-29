from argparse import ArgumentError
import basic_operators
import calc

version = 0.1


def show_help():
    print("Available operators :")
    print(calc.symbols)


print(f"Calculator {version} by rpopic2 | ? for help")
while 1:
    try:
        expr = input("> ")
    except (EOFError, KeyboardInterrupt):
        exit()
    if expr == "exit":
        exit()
    elif expr == '?':
        show_help()
        continue
    try:
        result = calc.main(expr)
        print(result)
    except Exception as e:
        print(e.args[1])
