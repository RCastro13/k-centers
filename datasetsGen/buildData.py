# ============
# Generate datasets. We choose the size big enough to see the scalability
# of the algorithms, but not too big to avoid too long running times
# ============
# import numpy as np
# from sklearn import datasets

# # Parâmetros
# n_samples = 1000
# seed = 42

# # Geração do dataset
# noisy_circles, _ = datasets.make_circles(
#     n_samples=n_samples, factor=0.5, noise=0.05, random_state=seed
# )

# # Salvando os pontos em um arquivo txt
# np.savetxt('noisy_circles.txt', noisy_circles, fmt='%f', delimiter=' ')

# # make_blobs
# blobs, _ = datasets.make_blobs(
#     n_samples=n_samples, centers=3, random_state=seed
# )
# np.savetxt('blobs.txt', blobs, fmt='%f', delimiter=' ')

# # make_moons
# moons, _ = datasets.make_moons(
#     n_samples=n_samples, noise=0.05, random_state=seed
# )
# np.savetxt('moons.txt', moons, fmt='%f', delimiter=' ')

# # make_classification
# classification, _ = datasets.make_classification(
#     n_samples=n_samples, n_features=2, n_informative=2, n_redundant=0,
#     random_state=seed
# )
# np.savetxt('classification.txt', classification, fmt='%f', delimiter=' ')

# # make_gaussian_quantiles
# gaussian_quantiles, _ = datasets.make_gaussian_quantiles(
#     mean=None, cov=1.0, n_samples=n_samples, n_features=2, n_classes=3, random_state=seed
# )
# np.savetxt('gaussian_quantiles.txt', gaussian_quantiles, fmt='%f', delimiter=' ')

# n_samples = 1200
# seed = 45

# # Geração do dataset
# noisy_circles, _ = datasets.make_circles(
#     n_samples=n_samples, factor=0.5, noise=0.05, random_state=seed
# )

# # Salvando os pontos em um arquivo txt
# np.savetxt('noisy_circles_2.txt', noisy_circles, fmt='%f', delimiter=' ')

# # make_blobs
# blobs, _ = datasets.make_blobs(
#     n_samples=n_samples, centers=3, random_state=seed
# )
# np.savetxt('blobs_2.txt', blobs, fmt='%f', delimiter=' ')

# # make_moons
# moons, _ = datasets.make_moons(
#     n_samples=n_samples, noise=0.05, random_state=seed
# )
# np.savetxt('moons_2.txt', moons, fmt='%f', delimiter=' ')

# # make_classification
# classification, _ = datasets.make_classification(
#     n_samples=n_samples, n_features=2, n_informative=2, n_redundant=0,
#     random_state=seed
# )
# np.savetxt('classification_2.txt', classification, fmt='%f', delimiter=' ')

# # make_gaussian_quantiles
# gaussian_quantiles, _ = datasets.make_gaussian_quantiles(
#     mean=None, cov=1.0, n_samples=n_samples, n_features=2, n_classes=3, random_state=seed
# )
# np.savetxt('gaussian_quantiles_2.txt', gaussian_quantiles, fmt='%f', delimiter=' ')

import time
import warnings
from itertools import cycle, islice

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn import cluster, datasets, mixture
from sklearn.neighbors import kneighbors_graph
from sklearn.preprocessing import StandardScaler

# ============
# Generate datasets. We choose the size big enough to see the scalability
# of the algorithms, but not too big to avoid too long running times
# ============
n_samples = 500
seed = 321
noisy_circles = datasets.make_circles(
    n_samples=n_samples, factor=0.8, noise=0.15, random_state=seed
)
noisy_moons = datasets.make_moons(n_samples=n_samples, noise=0.15, random_state=seed)
blobs = datasets.make_blobs(n_samples=n_samples, random_state=seed)
rng = np.random.RandomState(seed)
no_structure = rng.rand(n_samples, 2), None

# Anisotropicly distributed data
random_state = 12
X, y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
transformation = [[0.2, -0.6], [-0.4, 0.2]]
X_aniso = np.dot(X, transformation)
aniso = (X_aniso, y)

# blobs with varied variances
varied = datasets.make_blobs(
    n_samples=n_samples, cluster_std=[1.3, 1.8, 0.9], random_state=random_state
)

seed = 32
noisy_circles2 = datasets.make_circles(
    n_samples=n_samples, factor=0.8, noise=0.15, random_state=seed
)
noisy_moons2 = datasets.make_moons(n_samples=n_samples, noise=0.15, random_state=seed)
blobs2 = datasets.make_blobs(n_samples=n_samples, random_state=seed)
rng = np.random.RandomState(seed)
no_structure2 = rng.rand(n_samples, 2), None

# Anisotropicly distributed data
random_state = 12
X, y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
transformation = [[0.2, -0.6], [-0.4, 0.2]]
X_aniso = np.dot(X, transformation)
aniso2 = (X_aniso, y)

# blobs with varied variances
varied2 = datasets.make_blobs(
    n_samples=n_samples, cluster_std=[1.3, 1.8, 0.9], random_state=random_state
)

datasets = [
    (
        noisy_circles,
        {
            "damping": 0.77,
            "preference": -240,
            "quantile": 0.2,
            "n_clusters": 2,
            "min_samples": 7,
            "xi": 0.08,
        },
    ),
    (
        noisy_moons,
        {
            "damping": 0.75,
            "preference": -220,
            "n_clusters": 2,
            "min_samples": 7,
            "xi": 0.1,
        },
    ),
    (
        varied,
        {
            "eps": 0.18,
            "n_neighbors": 2,
            "min_samples": 7,
            "xi": 0.01,
            "min_cluster_size": 0.2,
        },
    ),
    (
        aniso,
        {
            "eps": 0.15,
            "n_neighbors": 2,
            "min_samples": 7,
            "xi": 0.1,
            "min_cluster_size": 0.2,
        },
    ),
    (blobs, {"min_samples": 7, "xi": 0.1, "min_cluster_size": 0.2}),
    (no_structure, {}),
    (
        noisy_circles2,
        {
            "damping": 0.77,
            "preference": -240,
            "quantile": 0.2,
            "n_clusters": 2,
            "min_samples": 7,
            "xi": 0.08,
        },
    ),
    (
        noisy_moons2,
        {
            "damping": 0.75,
            "preference": -220,
            "n_clusters": 2,
            "min_samples": 7,
            "xi": 0.1,
        },
    ),
    (
        varied2,
        {
            "eps": 0.18,
            "n_neighbors": 2,
            "min_samples": 7,
            "xi": 0.01,
            "min_cluster_size": 0.2,
        },
    ),
    (
        aniso2,
        {
            "eps": 0.15,
            "n_neighbors": 2,
            "min_samples": 7,
            "xi": 0.1,
            "min_cluster_size": 0.2,
        },
    ),
    (blobs2, {"min_samples": 7, "xi": 0.1, "min_cluster_size": 0.2}),
    (no_structure2, {}),
]

plt.show()

for i, (dataset, algo_params) in enumerate(datasets):
    try:
        X = dataset[0]
        y = dataset[1]
        data = np.concatenate([X, y.reshape(-1, 1)], axis=1)
        
        # Salvar no formato .txt com X Y label em cada linha
        with open(f"df_{i}.txt", 'w') as f:
            for row in data:
                f.write(f"{row[0]} {row[1]} {row[2]}\n")
    except:
        X = dataset[0]
        
        # Salvar no formato .txt com X Y em cada linha (sem o label)
        with open(f"df_{i}.txt", 'w') as f:
            for row in X:
                f.write(f"{row[0]} {row[1]}\n")
