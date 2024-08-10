import numpy as np

def minkowski_distance(a, b, p=2):
    return np.sum(np.abs(a - b) ** p, axis=1) ** (1 / p)

def initialize_centroids(X, k):
    indices = np.random.choice(X.shape[0], k, replace=False)
    return X[indices]

def assign_clusters(X, centroids, p=2):
    distances = np.array([minkowski_distance(X, centroid, p) for centroid in centroids])
    return np.argmin(distances, axis=0)

def update_centroids(X, labels, k):
    new_centroids = np.zeros((k, X.shape[1]))
    for i in range(k):
        cluster_points = X[labels == i]
        if len(cluster_points) > 0:
            new_centroids[i] = np.mean(cluster_points, axis=0)
    return new_centroids

def kmeans(X, k, p=2, max_iters=100):
    centroids = initialize_centroids(X, k)
    for _ in range(max_iters):
        labels = assign_clusters(X, centroids, p)
        new_centroids = update_centroids(X, labels, k)
        if np.allclose(centroids, new_centroids):
            break
        centroids = new_centroids
    return centroids, labels


# Dados exemplo
X = np.array([[1, 2], [1, 4], [1, 0],
                [10, 2], [10, 4], [10, 0]])

k = 2
p = 2  # Distância Euclidiana

centroids, labels = kmeans(X, k, p)

print("Centroids finais:")
print(centroids)
#as labels serão ignoradas, mas estão implementadas
#print("Labels:")
#print(labels)