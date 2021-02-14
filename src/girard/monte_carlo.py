import numpy as np
from girard import sampling

def all_coordinates_are_positive(vec):
    return all(map(lambda pos: pos >= 0, vec))

def estimate_solid_angle(spanning_matrix, sample_size):
    dim = len(spanning_matrix)
    inverse = np.linalg.inv(spanning_matrix)
    points_inside_cone = 0
    for i in range(sample_size):
        sample_point = np.matrix(sampling.sample_hypersphere_point(dim)).T
        transformed_point = inverse * sample_point
        if all_coordinates_are_positive(transformed_point):
            points_inside_cone += 1
    return points_inside_cone / sample_size
