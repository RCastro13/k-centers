import matplotlib.pyplot as plt
import numpy as np
import random
import time
from sklearn.metrics import silhouette_score, adjusted_rand_score
import sys

# Função de distância de Minkowski
def minkowski(p1, p2, p):
    p1 = np.array(p1)
    p2 = np.array(p2)
    result = np.sum(np.abs(p1 - p2) ** p)
    return result ** (1 / p)

# Função para calcular a maior distância em um conjunto de pontos
def max_dist(S):
    max_distance = -1
    for i in S:
        for j in S:
            curr = minkowski(i, j, 2)
            if not np.array_equal(i, j) and curr > max_distance:
                max_distance = curr
    return max_distance

# Função para calcular o raio da solução
def calculate_solution_radius(points, centers, p):
    max_radius = 0
    for point in points:
        min_distance = float('inf')
        for center in centers:
            dist = minkowski(point, center, p)
            if dist < min_distance:
                min_distance = dist
        if min_distance > max_radius:
            max_radius = min_distance
    return max_radius

# Função para atribuir rótulos de cluster aos pontos
def assign_clusters(points, centers):
    labels = []
    for point in points:
        min_distance = float('inf')
        cluster_label = -1
        for i, center in enumerate(centers):
            dist = minkowski(point, center, 2)
            if dist < min_distance:
                min_distance = dist
                cluster_label = i
        labels.append(cluster_label)
    return np.array(labels)

# Função principal
def main(filename):
    # Ler dados do arquivo
    data = np.loadtxt(filename)

    x = data[:, 0]
    y = data[:, 1]

    # Inicialização
    k = 3
    rmax = max_dist(data)
    left = 0
    right = rmax
    print('rmax:', rmax)
    C = []
    
    # Medir o tempo de execução
    start_time = time.time()

    # Enquanto L e R não convergirem para valores próximos
    while abs(left - right) > 0.00001:
        r = (left + right) / 2
        C = []
        S = data.copy()
        
        while len(S) > 0 and len(C) < k:
            s = random.randint(0, len(S) - 1)
            C.append(S[s])
            to_remove = [p for p in range(len(S)) if minkowski(S[p], S[s], 2) <= 2 * r]
            S = np.delete(S, to_remove, axis=0)
        
        if len(C) <= k:
            right = r
        else:
            left = r

    centers_x = [center[0] for center in C]
    centers_y = [center[1] for center in C]

    # Calcular o raio da solução
    points = list(zip(x, y))
    centers = list(zip(centers_x, centers_y))
    radius = calculate_solution_radius(points, centers, 2)
    print(f"Raio da solução: {radius}")

    # Atribuir rótulos aos pontos
    labels = assign_clusters(points, centers)

    # Calcular a silhueta e o índice de Rand ajustado
    silhouette_avg = silhouette_score(data, labels)
    adjusted_rand = adjusted_rand_score(labels, labels)
    print(f"Silhueta: {silhouette_avg}")
    print(f"Índice de Rand Ajustado: {adjusted_rand}")

    # Medir o tempo total de execução
    execution_time = time.time() - start_time
    print(f"Tempo gasto na execução: {execution_time:.4f} segundos")

    # Plotar os clusters e centros
    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(x, y, c=labels, cmap='viridis', edgecolor='k')
    plt.scatter(centers_x, centers_y, color='red', marker='x', s=100, label='Centros')
    plt.title('Clusters e Centros')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend()
    plt.colorbar(scatter, label='Cluster ID')
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <caminho_para_o_arquivo>")
    else:
        main(sys.argv[1])
