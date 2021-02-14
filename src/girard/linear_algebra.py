from decimal import Decimal
from numpy import dot
from numpy.linalg import norm
from toolz import reduce

#calculates the vector,vector exponentiations:
#for a, m in R^d, a^m is:
# \prod_{i = 0}^d a_i ^ m_i
def vector_vetor_exp(alpha, m):
    return Decimal(reduce(lambda a1, a2: a1 * a2, map(lambda a_m: a_m[0]**a_m[1], zip(alpha, m))))

#normalizes a vector v
def normalize(v):
    two_norm = norm(v)
    return list(map(lambda x: x / two_norm, v))

# given a vector m in R^\binom{n}{2}, given as (m_01; m_02; ...; m_0,n-1; m_12; ...; m_n-2,n-1), acesses the positions m_ij.
def access_vector_dim_n_choose_two(m, n, i, j):
    assert i < n, "Positions must be smaller than the dimension"
    assert j < n, "Positions must be smaller than the dimension"
    assert i != j, "Not defined when i == j"

    if i > j:
        return access_vector_dim_n_choose_two(m, n, j, i)
    l = int((n - 1) * i - i*(i-1)/2)
    return m[l + j - i -1]

# Given a vector m_tuple of dimension \binom{n}{2}, returns the sum
# of all entries of the form m_tuple[i][j] for a fixed i
def sum_of_entries_indexed_by_i(m_tuple, n, i):
    return sum([access_vector_dim_n_choose_two(m_tuple, n, i, j) for j in range(n) if i != j])

# compute the pairwise dot products (the dihedral angles) between the spanning vectors of the cone
def pairwise_dot_products(cone_vectors):
    n = len(cone_vectors)
    return [dot(cone_vectors[i], cone_vectors[j]) for i in range(n) for j in range(i + 1, n) if i != j]
