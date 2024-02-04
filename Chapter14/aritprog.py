import itertools
from decimal import Decimal


def aritprog_gen(begin, step, end=None):
    first = type(begin + step)(begin)
    ap_gen = itertools.count(first, step)
    if end is not None:
        ap_gen = itertools.takewhile(lambda n: n < end, ap_gen)
    return ap_gen


if __name__ == "__main__":
    ap = aritprog_gen(0, 1, 3)
    print(list(ap))
    ap = aritprog_gen(0, Decimal('.1'), 3)
    print(list(ap))
