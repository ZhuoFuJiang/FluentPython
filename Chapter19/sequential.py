from time import perf_counter
from typing import NamedTuple
from primes import is_prime, NUMBERS


class Result(NamedTuple):
    prime: bool
    elapsed: float


def check(n: int) -> Result:
    t0 = perf_counter()
    prime = is_prime(n)
    return Result(prime, perf_counter() - t0)


def main() -> None:
    print(f"Checking len{NUMBERS} numbers sequentially:")
    # perf_counter 返回性能计数器的值（以小数秒为单位）作为浮点数，即具有最高可用分辨率的时钟，以测量短持续时间
    t0 = perf_counter()
    for n in NUMBERS:
        prime, elapsed = check(n)
        label = 'P' if prime else ' '
        print(f"{n: 18} {label} {elapsed: 9.6f}s")
    elapsed = perf_counter() - t0
    print(f"Total time: {elapsed: .2f}s")


if __name__ == "__main__":
    main()
