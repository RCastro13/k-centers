import matplotlib.pyplot as plt
import numpy as np
import random
import time
import argparse
from sklearn.metrics import silhouette_score, adjusted_rand_score

#função que calcula a distância de Minkowski
def minkowskiDistance(p1, p2, p):
    p1 = np.array(p1)
    p2 = np.array(p2)
    result = np.sum(np.abs(p1 - p2) ** p)
    return result ** (1 / p)

# Parser para os argumentos de linha de comando
parser = argparse.ArgumentParser(description='K-centros 2-aproximado com visualização.')
parser.add_argument('filename', type=str, help='Nome do arquivo de entrada com os dados.')
args = parser.parse_args()

# Ler dados do arquivo
data = np.loadtxt(args.filename)
start_time = time.time()
x = data[:, 0]
y = data[:, 1]

#inicialização
used = [False for _ in range(len(x))]
centers_x = []
centers_y = []

#qdt de centros
k = 5

#escolher o primeiro centro arbitrariamente
C = [random.randint(0, len(x) - 1)]

#algoritmo guloso de k-centros 2-aproximado (segundo algoritmo ensinado)
while len(C) < k:
    s = -1
    max_dist = -1
    for i in range(len(x)):
        if used[i]:
            continue
        min_dist = float('inf')
        for j in C:
            dist = minkowskiDistance([x[i], y[i]], [x[j], y[j]], 2)
            if dist < min_dist:
                min_dist = dist
        #procurando a maior distância entre um ponto e seu centro mais próximo
        if min_dist > max_dist:
            max_dist = min_dist
            s = i
    #quando encontrar, salva
    C.append(s)
    used[s] = True

for i in C:
    centers_x.append(x[i])
    centers_y.append(y[i])

centers_x = np.array(centers_x)
centers_y = np.array(centers_y)

#calcula o raio da solução
def solutionRadius(points, centers, p):
    max_radius = 0
    for point in points:
        min_distance = float('inf')
        for center in centers:
            dist = minkowskiDistance(point, center, p)
            if dist < min_distance:
                min_distance = dist
        if min_distance > max_radius:
            max_radius = min_distance
    return max_radius

points = list(zip(x, y))
centers = list(zip(centers_x, centers_y))
radius = solutionRadius(points, centers, 2)
print(f"Raio da solução: {radius}")

#atribuir cores diferentes aos pontos de cada cluster
def assignClusters(points, centers):
    labels = []
    for point in points:
        min_distance = float('inf')
        cluster_label = -1
        for i, center in enumerate(centers):
            dist = minkowskiDistance(point, center, 2)
            if dist < min_distance:
                min_distance = dist
                cluster_label = i
        labels.append(cluster_label)
    return np.array(labels)

labels = assignClusters(points, centers)

# Cálculo da Silhueta
silhouette_avg = silhouette_score(points, labels)
print(f"Silhueta: {silhouette_avg}")

# Para o cálculo do Índice de Rand Ajustado, precisamos de labels verdadeiros
# Neste exemplo, usaremos os próprios labels calculados, mas normalmente isso seria comparado com a ground truth
adjusted_rand = adjusted_rand_score(labels, labels)
print(f"Índice de Rand Ajustado: {adjusted_rand}")

end_time = time.time()
execution_time = end_time - start_time
print(f"Tempo de execução: {execution_time:.4f} segundos")

plt.figure(figsize=(8, 6))
scatter = plt.scatter(x, y, c=labels, cmap='viridis', edgecolor='k')
plt.scatter(centers_x, centers_y, color='red', marker='x', s=100, label='Centros')

plt.title('Clusters e Centros')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.colorbar(scatter, label='Cluster ID')

plt.show()