import numpy as np

from math import sqrt
from numpy import linalg as npla
from scipy.optimize import linprog


def diagonalize_symmetric_matrix(M):
    eigenvalues, eigenvectors = npla.eig(M)

    diagonal_matrix = np.matrix(np.diagflat(eigenvalues))
    orthogonal_matrix = eigenvectors.T # the columns of orthogonal_matrix are the eigenvectors

    return orthogonal_matrix, diagonal_matrix


def square_root_positive_semidefinite_matrix(M):
    eigenvalues, orthogonal_eigenvectors = npla.eig(M)

    is_positive_semidefinite = all([x >= 0 for x in eigenvalues])

    if not is_positive_semidefinite:
        raise ValueError('The matrix must be positive semidefinite (have non-negative eigenvalues)')

    diagonal_square_root = np.matrix(np.diagflat([sqrt(x) for x in eigenvalues]))

    return orthogonal_eigenvectors * diagonal_square_root * orthogonal_eigenvectors.T


def flip_coin():
    return np.random.rand() > 0.5


def ones_vec(d):
    return np.matrix([1 for i in range(d)]).T


def fill_vertex_neighborhood(vertex_label, adjacency_matrix):
    neighborhood = adjacency_matrix[vertex_label].A1

    while True:
        for idx in range(adjacency_matrix.shape[0]):
            if idx != vertex_label and neighborhood[idx] == 0 and flip_coin():
                adjacency_matrix[vertex_label, idx] = adjacency_matrix[idx, vertex_label] = 1

        if sum(neighborhood) >= 2:
            break


def generate_graph(d):
    adjacency_matrix = np.matrix(np.zeros((d,d)))

    for label in range(d):
        fill_vertex_neighborhood(label, adjacency_matrix)

    return adjacency_matrix


def build_linear_constraints(graph):
    nvertices = graph.shape[0]
    linearlized_index = 0
    variable_mapping = {}
    rows = []

    for i in range(nvertices):
        for j in range(i + 1, nvertices):
            if i != j and graph[i, j] == 1:
                variable_mapping[linearlized_index] = (i, j)
                linearlized_index += 1

    for i in range(nvertices):
        rows.append([1 if i in variable_mapping[j] else 0 for j in range(linearlized_index)])

    return np.matrix(rows), variable_mapping


def generate_random_weighted_graph(d):
    g = generate_graph(d)
    linear_constraints, variable_mapping = build_linear_constraints(g)
    nedges = len(variable_mapping)

    random_objective_function = np.matrix([int(x * 10) + 1 for x in np.random.rand(nedges)]).T
    all_ones_obj = ones_vec(nedges)

    weights = linprog(c=all_ones_obj, A_eq=linear_constraints, b_eq=ones_vec(d)).x

    for linearlized_index, vertex_pair in variable_mapping.items():
        v = vertex_pair[0]
        u = vertex_pair[1]
        g[v, u] = g[u, v] = weights[linearlized_index]

    return g


def Identity(d):
    return np.matrix(np.diagflat([1 for i in range(d)]))


def trim_laplacian(g):
    g2 = g.copy()

    g2 = np.delete(g2, 0, axis=0)
    g2 = np.delete(g2, 0, axis=1)

    return g2


def generate_random_convergent_cone(d):
    G = generate_random_weighted_graph(d + 1)
    L = Identity(d + 1) - G
    T = trim_laplacian(L)
    VTV = 2*Identity(d) - T
    return square_root_positive_semidefinite_matrix(VTV)


def check(d):
    V = generate_random_convergent_cone(d)
    VTV = V.T * V
    M = 2 * Identity(d) - VTV
    return min(np.linalg.eigvals(M))
