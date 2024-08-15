import pandas as pd

# Função para ler o arquivo e criar o DataFrame
def criar_dataset(arquivo_txt):
    # Lista para armazenar as linhas do dataset
    dados = []

    # Abrir o arquivo e ler linha por linha
    with open(arquivo_txt, 'r') as arquivo:
        for linha in arquivo:
            # Remover espaços em branco e quebrar a linha em itens
            itens = linha.strip().split()
            
            # Convertendo cada item para o tipo correspondente
            algoritmo = int(itens[0])
            numCentros = int(itens[1])
            p = int(itens[2])
            instancia = str(itens[3])
            tempoExecucao = float(itens[4])
            raio = float(itens[5])
            silhueta = float(itens[6])
            indiceRand = float(itens[7])
            percentRaio = float(itens[8])
            
            # Adicionando a linha de dados à lista
            dados.append([algoritmo, numCentros, p, instancia, tempoExecucao, raio, silhueta, indiceRand, percentRaio])

    # Criar o DataFrame a partir da lista de dados
    colunas = ['algoritmo', 'numCentros', 'p', 'instancia', 'tempoExecucao', 'raio', 'silhueta', 'indiceRand', 'percentRaio']
    df = pd.DataFrame(dados, columns=colunas)
    
    return df

# Exemplo de uso
arquivo_txt = 'resultados.txt'  # Caminho para o arquivo .txt
df = criar_dataset(arquivo_txt)
print(df)