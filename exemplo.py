def media(*args, geometrica=False):
    """
    Calcula a média dos números x e y.
    """ 
    if geometrica:
        return prod(args) ** (1 / len(args))
    else:
        return sum(args) / len(args)


def prod(xs):
    """
    Calcula o produto da sequências de xs
    """
    prod = 1.0
    for x in xs:
        prod *= x
    return prod


def main():
    nums = []
    while (x := input(f'x{len(nums)}: ')):
        nums.append(float(x))
    
    print("Resultado: %s" % media(*nums))


if __name__ == '__main__':
    main()
