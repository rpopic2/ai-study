# def calculate(input):
#     augend = int(input[0])
#     addend = int(input[2])
#     return augend + addend

def calculate(input):
    augend, expr, addend = input.partition('+')
    return int(augend) + int(addend)

if __name__ == "__main__":
    import sys
    x= calculate(sys.argv[1])
    print(x)
