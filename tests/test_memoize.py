from pytest import mark

from solidus import memoize as m


@mark.parametrize('n, fact', [
    (0, 1),
    (1, 1),
    (5, 120),
    (7, 5040)
])
def test_factorial(n, fact):
    assert m.factorial(n) == fact


@mark.parametrize('n, power', [
    (0, 1),
    (1, 2),
    (5, 32),
    (7, 128),
    (10, 1024)
])
def test_power_of_two(n, power):
    assert m.power_of_two(n) == power


@mark.parametrize('n, odd_fact', [
    (2, 1),
    (4, 3),
    (8, 105),
    (10, 945)
])
def test_odd_factorial(n, odd_fact):
    assert m.odd_factorial(n) == odd_fact


def fill_vertex_neighborhood(vertex_label, adjacency_matrix):
    neighborhood = adjacency_matrix[vertex_label].A1

    if idx != vertex_label and val == 0 and flip_coin():
        adjacency_matrix[vertex_label, idx] = adjacency_matrix[idx, vertex_label] = 1

    while sum(neighborhood) < 2:
        random_vertex = int(np.random.rand() * adjacency_matrix.shape[0])
        if random_vertex != vertex_label and neighborhood[random_vertex] == 0:
            adjacency_matrix[vertex_label, idx] = adjacency_matrix[idx, vertex_label] = 1
