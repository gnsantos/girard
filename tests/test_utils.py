from math import sqrt, pi, isclose
from pytest import mark

from solidus import utils as u


SQRT_PI = sqrt(pi)


@mark.parametrize('n, gamma', [
    (0, SQRT_PI),
    (1, 1),
    (5, 2),
    (13, 720),
    (2, SQRT_PI / 2),
    (10, 945 * SQRT_PI / 32)
])
def test_gamma(n, gamma):
    assert isclose(u.gamma_n_plus_1_over_2(n), gamma)
