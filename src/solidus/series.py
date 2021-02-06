import numpy as np

from math import pi, sqrt, exp
from functools import reduce
from numpy import matrix, arccos
from numpy.linalg import inv, det
from decimal import *

from solidus import linear_algebra as la, memoize as mem, utils

#term of the hypergeometric series in dimension \binom{n}{k}.
# a and alpha are vectors in dimension \binom{n}{k}
def series_term(m_tuple, alpha, n):
    alpha_to_the_m = la.vector_vetor_exp(alpha, m_tuple)
    sum_entries = sum(m_tuple)
    sign = (-1) ** sum_entries
    power = mem.power_of_two(sum_entries)
    fact = reduce(lambda a,b: a*b, map(mem.factorial, m_tuple))
    gamma_prod = utils.gamma_product(m_tuple, n)
    return (alpha_to_the_m * sign * power * gamma_prod) / fact

# function that puts together all previous components to implement Ribando"s formula for the solid angle
def solid_angle(spanning_matrix, max_weight):
    cone_vectors = spanning_matrix.T.tolist()
    cone_vectors = list(map(la.normalize, cone_vectors))
    n = len(cone_vectors)
    alpha = la.pairwise_dot_products(cone_vectors)
    v_matrix = matrix(cone_vectors).T

    det_V = abs(det(v_matrix))

    pi_term = (4*pi)**(n/2.0)

    constant_term = Decimal(det_V / pi_term)
    series_dimension = int(n*(n-1)/2)
    inputs = utils.generate_tuples(series_dimension, max_weight)
    series = sum(map(lambda m: series_term(m, alpha, n), inputs))
    return constant_term * series
