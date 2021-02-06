from decimal import Decimal

memoization = {
    "factorial": {"cache": {0: Decimal(1), 1: Decimal(1)},
                  "step": 1, "factor": lambda x: Decimal(x),
                  "max": 1},
    "odd_factorial": {"cache": {2: Decimal(1), 4: Decimal(3)},
                      "step": 2, "factor": lambda x: Decimal(x - 1),
                      "max": 4},
    "power_of_two": {"cache": {0: Decimal(1), 1: Decimal(2)},
                     "step": 1, "factor": lambda x: Decimal(2),
                     "max": 1}
}


def _generic_memoized_fn(n, fn_type):
    cache, step, factor, max_memoized = memoization[fn_type].values()

    if n in cache:
        return cache[n]

    for value in range(max_memoized, n + 1, step):
        fn = factor(value) * cache[value - step]
        cache[value] = fn

    return cache[n]


def factorial(n):
    return _generic_memoized_fn(n, fn_type="factorial")


def power_of_two(n):
    return _generic_memoized_fn(n, fn_type="power_of_two")


def odd_factorial(n):
    assert n % 2 == 0, "Input must be an even number"
    return _generic_memoized_fn(n, fn_type="odd_factorial")
