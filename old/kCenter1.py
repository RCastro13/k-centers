#Algoritmo 2-Aproximado com Refinamento de Intervalo para o Raio Ótimo
import numpy as np

def minkowski_distance_matrix(X, p=2):
    dist_matrix = np.zeros((X.shape[0], X.shape[0]))
    for i in range(X.shape[0]):
        for j in range(i + 1, X.shape[0]):
            dist_matrix[i, j] = dist_matrix[j, i] = np.linalg.norm(X[i] - X[j], ord=p)
    return dist_matrix

def is_valid_k_center(dist_matrix, k, r):
    covered = np.zeros(dist_matrix.shape[0], dtype=bool)
    for _ in range(k):
        uncovered_indices = np.where(~covered)[0]
        if len(uncovered_indices) == 0:
            break
        center = uncovered_indices[0]
        covered |= dist_matrix[center] <= r
    return covered.all()

def k_centers_refinement(X, k, p=2, tolerance=1e-3):
    dist_matrix = minkowski_distance_matrix(X, p)
    low, high = 0, np.max(dist_matrix)
    while high - low > tolerance:
        mid = (low + high) / 2
        if is_valid_k_center(dist_matrix, k, mid):
            high = mid
        else:
            low = mid
    return high

# Exemplo de uso
if __name__ == "__main__":
    X = np.array([[1, 2], [1, 4], [1, 0],
                  [10, 2], [10, 4], [10, 0]])
    
    k = 2
    p = 2  # Distância Euclidiana
    tolerance = 1e-3
    
    raio_otimo = k_centers_refinement(X, k, p, tolerance)
    
    print("Raio ótimo aproximado:")
    print(raio_otimo)
