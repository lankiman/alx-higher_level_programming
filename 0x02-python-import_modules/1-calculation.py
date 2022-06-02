#!/usr/bin/python3

if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    ad = add(a, b)
    sb = sub(a, b)
    ml = mul(a, b)
    dv = div(a, b)

    print("{} + {} = {}".format(a, b, ad))
    print("{} - {} = {}".format(a, b, sb))
    print("{} * {} = {}".format(a, b, ml))
    print("{} / {} = {}".format(a, b, dv))
