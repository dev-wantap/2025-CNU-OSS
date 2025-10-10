def func(x, a, b):
    result = x * a * a + b
    return result


def main():
    a = int(input("a  : "))
    b = int(input("b  : "))
    max = int(input("Max: "))

    for i in range(max+1):
        print(f"{a}x{a}x{i} + {b} = {func(i, a, b)}")


main()
