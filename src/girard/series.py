import numpy as np
from math import pi, sqrt
from functools import reduce
from numpy.linalg import det
from decimal import *
from girard import linear_algebra as la, memoize as mem, utils, series_convergence as sc

# Term of the hypergeometric series in dimension \binom{n}{k}.
# m_tuple and alpha are vectors in dimension \binom{n}{k}
def series_term(m_tuple, alpha, n):
    alpha_to_the_m = la.vector_vetor_exp(alpha, m_tuple)
    sum_entries = sum(m_tuple)
    sign = (-1) ** sum_entries
    power = mem.power_of_two(sum_entries)
    fact = reduce(lambda a,b: a*b, map(mem.factorial, m_tuple))
    gamma_prod = utils.gamma_product(m_tuple, n)
    return (alpha_to_the_m * sign * power * gamma_prod) / fact

# Function that implements Ribando"s formula for the solid angle
def solid_angle(spanning_matrix, eps, max_weight=50):
    cone_vectors = list(map(la.normalize, spanning_matrix.T.tolist()))
    dimension = len(cone_vectors)

    alpha = la.pairwise_dot_products(cone_vectors)
    normalized_spanning_matrix = np.matrix(cone_vectors).T

    series_will_converge = sc.check_convergence(normalized_spanning_matrix)
    if not series_will_converge:
        raise ValueError("The cone inputed is not within the region of convergence of the hypergeometric series. Use the monte_carlo module instead.")

    det_V = abs(np.linalg.det(normalized_spanning_matrix))
    pi_term = (4*np.pi)**(dimension/2.0)
    constant_term = Decimal(det_V / pi_term)

    series_dimension = int(dimension*(dimension-1)/2)
    inputs = utils.tuple_generator(series_dimension)
    max_number_of_tuples = utils.number_of_d_tuples_with_max_weight_k(series_dimension, max_weight)

    approx = 0
    its = 0
    compare = 0
    should_compare = False

    while its < max_number_of_tuples:
        mtuple = next(inputs)
        term = series_term(mtuple, alpha, dimension)
        approx += term
        angle = constant_term*approx
        its += 1

        if should_compare and (its % 10000 == 0):
            rel = abs(compare - angle)/abs(angle)
            if rel < eps:
                break

        if its % 10000 == 0:
            compare = angle
            should_compare = True

    return constant_term * approx
