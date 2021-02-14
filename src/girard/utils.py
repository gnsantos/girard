from decimal import Decimal
from toolz import reduce

from girard import linear_algebra as la, memoize as mem

# Given a vector (m_11,m_12,...,m_1n,m_23,...,m_n-1,n) in R^\binom{n}{k},
# compute the following product of gamma functions:
# We say the entries indexed by i are the ones with format m_ij, for j != i.
# Let s_i be the sum of the entries indexed by i.
# The function computes \prod_{i = 1}^n \Gamma((s_i + 1)/2)
def gamma_product(m_tuple, n):
    sum_of_indexed_entries_by_position = [la.sum_of_entries_indexed_by_i(m_tuple, n, i) for i in range(n)]
    product_of_gammas = reduce(lambda x, y: x * y, map(mem.gamma_n_plus_1_over_2, sum_of_indexed_entries_by_position))
    return Decimal(product_of_gammas)

# Explores the space of natural tuples in dimension d as a graph.
# Breadth-First Search is used to traverse the graph.
# Yield is used to produce a generator: tuples will be generated as required.
def tuple_generator(d):
    zero = tuple(0 for i in range(d))
    tuples = set()
    tuples.add(zero)
    to_process = [zero]

    while True:
        t = to_process.pop(0)
        yield t

        for pos, val in enumerate(t):
            derived_tuple = t[:pos] + (val + 1,) + t[pos + 1:]

            if derived_tuple in tuples:
                continue

            tuples.add(derived_tuple)
            to_process.append(derived_tuple)

# Computes how many tuples in dimension d have 1-norm k or less
def number_of_d_tuples_with_max_weight_k(d, k):
    return mem.factorial(d+k) / ( mem.factorial(d) * mem.factorial(k) )
