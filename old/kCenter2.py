#Algoritmo 2-Aproximado com Maximização da Distância Entre Centros
import numpy as np

def minkowski_distance_matrix(X, p=2):
    dist_matrix = np.zeros((X.shape[0], X.shape[0]))
    for i in range(X.shape[0]):
        for j in range(i + 1, X.shape[0]):
            dist_matrix[i, j] = dist_matrix[j, i] = np.linalg.norm(X[i] - X[j], ord=p)
    return dist_matrix

def farthest_first_traversal(X, k, p=2):
    dist_matrix = minkowski_distance_matrix(X, p)
    centers = [np.random.choice(X.shape[0])]
    for _ in range(1, k):
        dist_to_closest_center = np.min(dist_matrix[centers], axis=0)
        next_center = np.argmax(dist_to_closest_center)
        centers.append(next_center)
    return centers

# Exemplo de uso
if __name__ == "__main__":
    X = np.array([[1, 2], [1, 4], [1, 0],
                  [10, 2], [10, 4], [10, 0]])
    
    k = 2
    p = 2  # Distância Euclidiana
    
    centros = farthest_first_traversal(X, k, p)
    
    print("Índices dos centros selecionados:")
    print(centros)
    print("Coordenadas dos centros:")
    print(X[centros])
    