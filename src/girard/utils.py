import numpy as np

from decimal import Decimal
from math import sqrt, pi
from numpy import dot
from toolz import reduce

from datetime import datetime

from girard import linear_algebra as la, memoize as mem

def sampleHyperspherePoint(dim):
    gaussianSamples = np.random.normal(0, 1, dim)
    return la.normalize(gaussianSamples)


def gamma_n_plus_1_over_2(n):
    if n % 2 == 1:
        return mem.factorial((n - 1) // 2)
    else:
        sqrt_pi = Decimal(sqrt(pi))
        if n == 0:
            return sqrt_pi

        half_n = n // 2
        return (sqrt_pi / mem.power_of_two(half_n)) * mem.odd_factorial(n)


def sum_of_entries_indexed_by_i(m_tuple, n, i):
    return sum([la.access_vector_dim_n_choose_two(m_tuple, n, i, j) for j in range(n) if i != j])


#given a vector m in R^\binom{n}{k}, given as (m_11,m_12,...,m_1n, m_23,...,m_n-1,n), compute the following product of gamma functions:
# We say the entries indexed by i are the ones with format m_ij, for j != i.
# Let s_i be the sum of the entries indexed by i.
# The function computes \prod_{i = 1}^n \Gamma((s_i + 1)/2)
def gamma_product(m_tuple, n):
    sum_of_indexed_entries_by_position = [sum_of_entries_indexed_by_i(m_tuple, n, i) for i in range(n)]
    product_of_gammas = reduce(lambda x, y: x * y, map(gamma_n_plus_1_over_2, sum_of_indexed_entries_by_position))
    return Decimal(product_of_gammas)


# Explores the space of natural tuples in dimension d as a graph.
# Breadth-First Search is used to traverse the graph
def generate_tuples(d, k):
    zero = tuple(0 for i in range(d))
    tuples = set()

    tuples.add(zero)
    to_process = [zero]

    number_of_tuples = mem.factorial(d + k)/(mem.factorial(k) * mem.factorial(d))
    current_tuples = 1

    while current_tuples < number_of_tuples:
        t = to_process.pop(0)

        for pos, val in enumerate(t):
            derived_tuple = t[:pos] + (val + 1,) + t[pos + 1:]

            if derived_tuple in tuples:
                continue

            tuples.add(derived_tuple)
            to_process.append(derived_tuple)
            current_tuples += 1

    return tuples
