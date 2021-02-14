import numpy as np
from girard import monte_carlo as mc

def get_sample_std(omega, N):
    return np.sqrt(omega * (1 - omega) / N)

def get_confidence_interval_prediction(omega, N):
    std = get_sample_std(omega, N)
    return omega - 2*std, omega + 2*std

def get_sample_distribution_for_solid_angle(cone_vectors, samples_per_estimate, population_size):
    estimators = [mc.estimate_solid_angle(cone_vectors, samples_per_estimate) for i in range(population_size)]

    mean = np.mean(estimators)
    real_std = np.std(estimators)
    predicted_std = get_sample_std(mean, samples_per_estimate)

    return estimators, mean, real_std, predicted_std
