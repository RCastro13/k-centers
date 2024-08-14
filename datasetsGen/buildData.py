# ============
# Generate datasets. We choose the size big enough to see the scalability
# of the algorithms, but not too big to avoid too long running times
# ============
import numpy as np
from sklearn import datasets

# Parâmetros
n_samples = 1000
seed = 42

# Geração do dataset
noisy_circles, _ = datasets.make_circles(
    n_samples=n_samples, factor=0.5, noise=0.05, random_state=seed
)

# Salvando os pontos em um arquivo txt
np.savetxt('noisy_circles.txt', noisy_circles, fmt='%f', delimiter=' ')

# make_blobs
blobs, _ = datasets.make_blobs(
    n_samples=n_samples, centers=3, random_state=seed
)
np.savetxt('blobs.txt', blobs, fmt='%f', delimiter=' ')

# make_moons
moons, _ = datasets.make_moons(
    n_samples=n_samples, noise=0.05, random_state=seed
)
np.savetxt('moons.txt', moons, fmt='%f', delimiter=' ')

# make_classification
classification, _ = datasets.make_classification(
    n_samples=n_samples, n_features=2, n_informative=2, n_redundant=0,
    random_state=seed
)
np.savetxt('classification.txt', classification, fmt='%f', delimiter=' ')

# make_gaussian_quantiles
gaussian_quantiles, _ = datasets.make_gaussian_quantiles(
    mean=None, cov=1.0, n_samples=n_samples, n_features=2, n_classes=3, random_state=seed
)
np.savetxt('gaussian_quantiles.txt', gaussian_quantiles, fmt='%f', delimiter=' ')

n_samples = 1200
seed = 45

# Geração do dataset
noisy_circles, _ = datasets.make_circles(
    n_samples=n_samples, factor=0.5, noise=0.05, random_state=seed
)

# Salvando os pontos em um arquivo txt
np.savetxt('noisy_circles_2.txt', noisy_circles, fmt='%f', delimiter=' ')

# make_blobs
blobs, _ = datasets.make_blobs(
    n_samples=n_samples, centers=3, random_state=seed
)
np.savetxt('blobs_2.txt', blobs, fmt='%f', delimiter=' ')

# make_moons
moons, _ = datasets.make_moons(
    n_samples=n_samples, noise=0.05, random_state=seed
)
np.savetxt('moons_2.txt', moons, fmt='%f', delimiter=' ')

# make_classification
classification, _ = datasets.make_classification(
    n_samples=n_samples, n_features=2, n_informative=2, n_redundant=0,
    random_state=seed
)
np.savetxt('classification_2.txt', classification, fmt='%f', delimiter=' ')

# make_gaussian_quantiles
gaussian_quantiles, _ = datasets.make_gaussian_quantiles(
    mean=None, cov=1.0, n_samples=n_samples, n_features=2, n_classes=3, random_state=seed
)
np.savetxt('gaussian_quantiles_2.txt', gaussian_quantiles, fmt='%f', delimiter=' ')