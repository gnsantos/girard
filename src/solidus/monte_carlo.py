import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
from solidus import sampling


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


def get_sample_std(omega, N):
    return np.sqrt(omega * (1 - omega) / N)


def get_confidence_interval_prediction(omega, N):
    std = get_sample_std(omega, N)
    return omega - 2*std, omega + 2*std


def get_sample_distribution_for_solid_angle(cone_vectors, samples_per_estimate, population_size):
    estimators = [estimate_solid_angle(cone_vectors, samples_per_estimate) for i in range(population_size)]

    mean = np.mean(estimators)
    real_std = np.std(estimators)
    predicted_std = get_sample_std(mean, samples_per_estimate)

    return estimators, mean, real_std, predicted_std
