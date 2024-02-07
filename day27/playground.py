def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(5, 6, 7, 4, 2))


def calculate(**kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)



calculate(add=3, multiply=5)
