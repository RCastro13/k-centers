import matplotlib.pyplot as plt
import numpy as np
import random
import time
from sklearn.metrics import silhouette_score, adjusted_rand_score
import sys

# Função de distância de Minkowski
def minkowski(p1, p2):
    p=1
    p1 = np.array(p1)
    p2 = np.array(p2)
    result = np.sum(np.abs(p1 - p2) ** p)
    return result ** (1 / p)

# Função para calcular a maior distância em um conjunto de pontos
def max_dist(S):
    max_distance = -1
    for i in S:
        for j in S:
            curr = minkowski(i, j)
            if not np.array_equal(i, j) and curr > max_distance:
                max_distance = curr
    return max_distance

# Função para calcular o raio da solução
def calculate_solution_radius(points, centers):
    max_radius = 0
    for point in points:
        min_distance = float('inf')
        for center in centers:
            dist = minkowski(point, center)
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
            dist = minkowski(point, center)
            if dist < min_distance:
                min_distance = dist
                cluster_label = i
        labels.append(cluster_label)
    return np.array(labels)

# Função principal
def main(filename):
    # Executar o código 30 vezes
    # Ler dados do arquivo
    data = np.loadtxt(filename)

    x = data[:, 0]
    y = data[:, 1]
    true_labels = data[:, 2]  # Lendo os rótulos verdadeiros da terceira coluna
    # Inicialização
    k = 3
    #p = 2  # Parâmetro da distância de Minkowski
    rmax = max_dist(data[:, :2])
    print('rmax:', rmax)
    C = []
    percent = 0.08
    for i in range(30):
        print(f"\nExecução {i+1}/30")

        # Definir variáveis para as colunas 1 e 4
        algoritmo = 2  # 1=GULOSO, 2=PESQBIN, 3=KMEANS
        instancia = filename
        
        # Medir o tempo de execução
        start_time = time.time()
        
        raioDaVez = float('inf')
        left = 0
        right = rmax
        # Enquanto L e R não convergirem para valores próximos
        #while(left - right > 0.01):
        while raioDaVez / rmax > percent:
            r = (left + right) / 2
            C = []
            S = data[:, :2].copy()  # Usando apenas as colunas de coordenadas para clustering
            
            while len(S) > 0 and len(C) < k:
                s = random.randint(0, len(S) - 1)
                C.append(S[s])
                to_remove = [p for p in range(len(S)) if minkowski(S[p], S[s]) <= 2 * r]
                S = np.delete(S, to_remove, axis=0)

            raioDaVez = r
            
            if len(C) <= k:
                right = r
            else:
                left = r

        centers_x = [center[0] for center in C]
        centers_y = [center[1] for center in C]

        # Calcular o raio da solução
        points = list(zip(x, y))
        centers = list(zip(centers_x, centers_y))
        radius = calculate_solution_radius(points, centers)
        print(f"Raio da solução: {radius}")

        # Atribuir rótulos aos pontos
        labels = assign_clusters(points, centers)

        # Calcular a silhueta e o índice de Rand ajustado
        silhouette_avg = silhouette_score(data[:, :2], labels)
        rand = adjusted_rand_score(true_labels, labels)  # Comparar rótulos verdadeiros com os rótulos de cluster
        print(f"Silhueta: {silhouette_avg}")
        print(f"Índice de Rand Ajustado: {rand}")

        # Medir o tempo total de execução
        execution_time = time.time() - start_time
        print(f"Tempo gasto na execução: {execution_time:.4f} minutos")

        # Salvar resultados em um arquivo .txt
        result_file = 'resultados.txt'
        with open(result_file, 'a') as file:
            file.write(f"{algoritmo}\t{k}\t1\t{instancia}\t{execution_time:.4f}\t{radius:.4f}\t{silhouette_avg:.4f}\t{rand:.4f}\t{percent}\n")

        # Plotar os clusters e centros (apenas na última execução)
        if i == 29:
            plt.figure(figsize=(8, 6))
            scatter = plt.scatter(x, y, c=labels, cmap='viridis', edgecolor='k')
            plt.scatter(centers_x, centers_y, color='red', marker='x', s=100, label='Centros')
            plt.title('Clusters e Centros')
            plt.xlabel('Feature 1')
            plt.ylabel('Feature 2')
            plt.legend()
            plt.colorbar(scatter, label='Cluster ID')
            #plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <caminho_para_o_arquivo>")
    else:
        main(sys.argv[1])
