import numpy as np

fileNames = ['pontos_multivariados1.txt',
             'pontos_multivariados2.txt',
             'pontos_multivariados3.txt',
             'pontos_multivariados4.txt',
             'pontos_multivariados5.txt',
             'pontos_multivariados6.txt',
             'pontos_multivariados7.txt',
             'pontos_multivariados8.txt',
             'pontos_multivariados9.txt',
             'pontos_multivariados0.txt'
             ]

seeds = [42,43,44,45,46,47,48,49,50,51]
counter = 0

for i in range (10):
    # Definir parâmetros para a geração de pontos
    centros = np.array([[0, 0], [5, 5], [10, 0]])  # Centros para três grupos
    desvios = [0.5, 1.5, 3.0]  # Desvios padrão para controlar a sobreposição

    # Quantidade total de pontos e pontos por centro
    total_pontos = 800
    num_pontos_por_centro = total_pontos // len(centros)

    # Gerar pontos ao redor de cada centro
    np.random.seed(seeds[counter])  # Para reprodutibilidade
    pontos = []

    for centro, desvio in zip(centros, desvios):
        pontos_centro = np.random.normal(loc=centro, scale=desvio, size=(num_pontos_por_centro, 2))
        pontos.append(pontos_centro)

    # Concatenar todos os pontos
    pontos = np.vstack(pontos)

    # Salvar os pontos em um arquivo .txt
    np.savetxt(fileNames[counter], pontos, fmt="%.5f")
    counter = counter + 1
