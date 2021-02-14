from decimal import Decimal
from math import sqrt, pi

factorial_cache = {0: Decimal(1), 1: Decimal(1)}
def factorial(n):
    if n in factorial_cache:
        return factorial_cache[n]
    for value in range(max(factorial_cache.keys()), n + 1):
        factorial_cache[value] = Decimal(value) * factorial_cache[value - 1]
    return factorial_cache[n]

power_of_two_cache = {0: Decimal(1), 1: Decimal(2)}
def power_of_two(n):
    if n in power_of_two_cache:
        return power_of_two_cache[n]
    for value in range(max(power_of_two_cache.keys()), n + 1):
        power_of_two_cache[value] = Decimal(2) * power_of_two_cache[value - 1]
    return power_of_two_cache[n]

odd_fact_cache = {2: Decimal(1), 4: Decimal(3)}
def odd_factorial(n):
    if n in odd_fact_cache:
        return odd_fact_cache[n]
    for value in range(max(odd_fact_cache.keys()), n + 1, 2):
        odd_fact_cache[value] = Decimal(value - 1) * odd_fact_cache[value - 2]
    return odd_fact_cache[n]

def gamma_n_plus_1_over_2(n):
    if n % 2 == 1:
        return factorial((n - 1) // 2)
    else:
        sqrt_pi = Decimal(sqrt(pi))
        if n == 0:
            return sqrt_pi
        half_n = n // 2
        return (sqrt_pi / power_of_two(half_n)) * odd_factorial(n)
