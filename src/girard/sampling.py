import numpy as np
from girard import linear_algebra as la

def sample_hypersphere_point(dim):
    gaussianSamples = np.random.normal(0, 1, dim)
    return la.normalize(gaussianSamples)
Ma
def sample_cone_uniformly(dimension):
    np.matrix([sample_hypersphere_point(dimension) for i in range(dimension)]).T
