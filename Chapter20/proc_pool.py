import sys
from time import perf_counter
from typing import NamedTuple
from concurrent import futures
from Chapter19.primes import is_prime, NUMBERS


class PrimeResult(NamedTuple):
    n: int
    prime: bool
    elapsed: float


def check(n: int) -> PrimeResult:
    t0 = perf_counter()
    res = is_prime(n)
    return PrimeResult(n, res, perf_counter() - t0)


def main() -> None:
    if len(sys.argv) < 2:
        workers = None
    else:
        workers = int(sys.argv[1])

    executor = futures.ProcessPoolExecutor(workers)
    actual_workers = executor._max_workers

    print(f"Checking {len(NUMBERS)} numbers with {actual_workers} processes")
    t0 = perf_counter()
    numbers = sorted(NUMBERS, reverse=True)
    with executor:
        for n, prime, elapsed in executor.map(check, numbers):
            label = 'p' if prime else ' '
            print(f'{n:18} {label} {elapsed:9.6f}s')
    time = perf_counter() - t0
    print(f"Total time: {time:.2f}s")


if __name__ == "__main__":
    main()


