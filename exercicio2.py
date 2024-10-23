#Construa uma matriz A de tamanho 10 x 10 com valores inteiros e randômicos. Depois:
#a. Imprima o resultado da soma de todos os valores da matriz no terminal;
#b. E, criei uma nova matriz B, no qual cada item seja o valor da matriz A * 3;

import random

# Função para gerar a matriz 10x10 com valores randômicos
def gerar_matriz():
    matriz = []
    for i in range(10):
        linha = [random.randint(1, 100) for _ in range(10)]
        matriz.append(linha)
    return matriz

# Função para calcular a soma de todos os elementos da matriz
def soma_matriz(matriz):
    soma = 0
    for linha in matriz:
        soma += sum(linha)
    return soma

# Função para criar a matriz B onde cada elemento é o triplo de A
def criar_matriz_triplicada(matriz):
    matriz_b = []
    for linha in matriz:
        linha_b = [x * 3 for x in linha]
        matriz_b.append(linha_b)
    return matriz_b

# Função para imprimir uma matriz
def imprimir_matriz(matriz, nome):
    print(f"Matriz {nome}:")
    for linha in matriz:
        print(linha)

# Programa principal
def main():
    # Gerar matriz A com valores randômicos entre 1 e 100
    matriz_a = gerar_matriz()

    # Imprimir a matriz A
    imprimir_matriz(matriz_a, "A")
    
    # a) Soma de todos os valores da matriz A
    soma_total = soma_matriz(matriz_a)
    print(f"\nSoma de todos os valores da matriz A: {soma_total}\n")
    
    # b) Criar a matriz B (valores de A * 3)
    matriz_b = criar_matriz_triplicada(matriz_a)
    
    # Imprimir a matriz B
    imprimir_matriz(matriz_b, "B")

# Executar o programa
if __name__ == "__main__":
    main()