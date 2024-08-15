import numpy as np
import time
import argparse
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, adjusted_rand_score, rand_score
from scipy.spatial.distance import cdist

# Função para ler os pontos de um arquivo .txt, incluindo os labels verdadeiros
def read_points_and_labels_from_txt(file_path):
    points = []
    true_labels = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y, label = map(float, line.strip().split())
            points.append([x, y])
            true_labels.append(int(label))  # Armazena os rótulos verdadeiros como inteiros
    return np.array(points), np.array(true_labels)

# Função para calcular os raios dos clusters
def calculate_cluster_radii(points, labels, cluster_centers):
    radii = []
    for i, center in enumerate(cluster_centers):
        # Seleciona os pontos do cluster i
        cluster_points = points[labels == i]
        # Calcula a distância de cada ponto do cluster ao centro do cluster
        distances = np.linalg.norm(cluster_points - center, axis=1)
        # O raio é a distância máxima do ponto mais distante
        radii.append(np.max(distances))
    return radii

# Função para plotar os clusters e os raios
def plot_clusters_with_radii(points, labels, cluster_centers, radii):
    fig, ax = plt.subplots()
    
    # Plotar pontos e centros dos clusters
    scatter = ax.scatter(points[:, 0], points[:, 1], c=labels, cmap='viridis', marker='o', s=50, alpha=0.6, edgecolor='k')
    ax.scatter(cluster_centers[:, 0], cluster_centers[:, 1], c='red', marker='x', s=200, label='Centros')

    # Adicionar círculos com o raio dos clusters
    for i, (center, radius) in enumerate(zip(cluster_centers, radii)):
        circle = plt.Circle(center, radius, color='r', fill=False, linestyle='--', label=f'Raio Cluster {i+1}')
        ax.add_artist(circle)

    # Definições adicionais para o gráfico
    ax.set_title("K-Means Clustering com Raios dos Clusters")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.legend()
    plt.show()

# Função principal
def kmeans_clustering(file_path):
    # Defina o número de clusters
    n_clusters = 6  # Alterar o número de clusters conforme desejado
    
    # Ler pontos e rótulos verdadeiros do arquivo
    points, true_labels = read_points_and_labels_from_txt(file_path)
    
    # Aplicar o algoritmo de KMeans
    start_time = time.time()
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(points)
    execution_time = time.time() - start_time
    
    # Previsões do KMeans
    predicted_labels = kmeans.labels_
    cluster_centers = kmeans.cluster_centers_
    
    # Cálculo da silhueta
    silhouette_avg = silhouette_score(points, predicted_labels)
    
    # Cálculo do Índice de Rand Ajustado usando os rótulos verdadeiros e os rótulos previstos pelo KMeans
    rand_score_val = adjusted_rand_score(true_labels, predicted_labels)
    
    # Cálculo dos raios dos clusters
    radii = calculate_cluster_radii(points, predicted_labels, cluster_centers)
    
    # Impressão dos resultados
    print(f"Tempo de execução: {execution_time:.4f} segundos")
    print(f"Silhueta média: {silhouette_avg:.4f}")
    print(f"Índice de Rand Ajustado: {rand_score_val:.4f}")
    
    # Imprimir o maior raio entre os clusters
    max_radius = max(radii)
    print(f"Maior raio encontrado: {max_radius:.4f}")

    result_file = 'resultados.txt'
    empty = 0
    algoritmo = 3
    k = n_clusters
    instancia = file_path
    radius = max_radius
    with open(result_file, 'a') as file:
        file.write(f"{algoritmo}\t{k}\t0\t{instancia}\t{execution_time:.4f}\t{radius:.4f}\t{silhouette_avg:.4f}\t{rand_score_val:.4f}\t{empty}\n")
    
    # Plotar clusters com raios
    plot_clusters_with_radii(points, predicted_labels, cluster_centers, radii)

if __name__ == '__main__':
    # Definindo o parser de argumentos
    parser = argparse.ArgumentParser(description="K-Means clustering para pontos de um arquivo .txt")
    
    # Argumento: caminho do arquivo
    parser.add_argument('file_path', type=str, help="Caminho para o arquivo .txt contendo os pontos e os rótulos")
    
    # Parseando os argumentos
    args = parser.parse_args()
    
    # Executar a função de clustering
    kmeans_clustering(args.file_path)
