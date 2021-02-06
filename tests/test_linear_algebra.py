from numpy import dot
from pytest import mark

from girard import linear_algebra as la


@mark.parametrize('v1, v2, expected', [
    ([10], [5], 100000),
    ([3, 4], [3, 5], 27648),
    ([1, 2, 3], [6, 5, 2], 288)
])
def test_vector_vector_exp(v1, v2, expected):
    assert la.vector_vetor_exp(v1, v2) == expected


@mark.parametrize('vector, normalized', [
    ([3, 4], [0.6, 0.8]),
    ([12, 5], [0.9230769230769231, 0.38461538461538464])
])
def test_normalize(vector, normalized):
    assert la.normalize(vector) == normalized


@mark.parametrize('vector, base_dimension, i, j, value', [
    ([1], 2, 0 ,1, 1),
    ([1], 2, 1 ,0, 1),
    ([1, 4, 9], 3, 0, 1, 1),
    ([1, 4, 9], 3, 1, 0, 1),
    ([1, 4, 9], 3, 0, 2, 4),
    ([1, 4, 9], 3, 2, 0, 4),
    ([1, 4, 9], 3, 1, 2, 9),
    ([1, 4, 9], 3, 2, 1, 9),
    ([2, 4, 8, 16, 32, 64], 4, 0, 1, 2),
    ([2, 4, 8, 16, 32, 64], 4, 0, 2, 4),
    ([2, 4, 8, 16, 32, 64], 4, 0, 3, 8),
    ([2, 4, 8, 16, 32, 64], 4, 1, 2, 16),
    ([2, 4, 8, 16, 32, 64], 4, 1, 3, 32),
    ([2, 4, 8, 16, 32, 64], 4, 2, 3, 64)
])
def test_access_vector_dim_n_choose_two(vector, base_dimension, i, j, value):
    assert la.access_vector_dim_n_choose_two(vector, base_dimension, i, j) == value


@mark.parametrize('cone_vectors, pairwise_dots', [
    ([[1,2,3], [4,5,6], [7,8,9]], [32, 50, 122]),
    ([[1,2,3, 11], [4,5,6, 13], [7,8,9, 19], [23, 31, 57, 93]], [175, 259, 1279, 369, 1798, 2689]),
    ([[1,2,3, 10, 11], [4,5,6, 12, 13], [7,8,9, 19, 14], [23, 31, 57, 93, 16], [41, 42, 43, 32,42]],
     [295, 394, 1362, 1036, 532, 1913, 1562, 2913, 2206, 8344])
])
def test_pairwise_dor_products(cone_vectors, pairwise_dots):
    assert la.pairwise_dot_products(cone_vectors) == pairwise_dots


@mark.parametrize('cone_vectors', [
    [[1,2,3], [4,5,6], [7,8,9]],
    [[1,2,3, 11], [4,5,6, 13], [7,8,9, 19], [23, 31, 57, 93]],
    [[1,2,3, 10, 11], [4,5,6, 12, 13], [7,8,9, 19, 14], [23, 31, 57, 93, 16], [41, 42, 43, 32,42]]
])
def test_access_on_vector_of_pairwise_dots(cone_vectors):
    pairwise_dot = la.pairwise_dot_products(cone_vectors)

    for i in range(len(cone_vectors)):
        for j in range(len(cone_vectors)):
            if i == j:
                continue

            expected_value = dot(cone_vectors[i], cone_vectors[j])

            assert la.access_vector_dim_n_choose_two(pairwise_dot, len(cone_vectors), i, j) == expected_value
