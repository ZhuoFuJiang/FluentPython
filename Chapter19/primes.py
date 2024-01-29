import math
import time


NUMBERS = [3333333333333333, 4444444444444444, 5555555555555555,
           6666666666666666, 142702110479723, 7777777777777777,
           299593572317531, 9999999999999999, 3333333333333301,
           3333335652092209, 4444444488888889, 4444444444444423,
           5555553133149889, 5555555555555503, 6666666666666719,
           6666667141414921, 7777777536340681, 7777777777777753,
           9999999999999917]


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    root = math.isqrt(n)
    for i in range(3, root+1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    st = time.time()
    is_prime(5000111000222021)
    print(time.time() - st)

