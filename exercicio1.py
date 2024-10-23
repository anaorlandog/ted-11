#Faça um algoritmo para ler 10 números e armazenar em um vetor VET, verificar e escrever se existem
#números repetidos no vetor VET e em que posições se encontram.

def ler_numeros():
    VET = []
    for i in range(10):
        num = int(input(f"Digite o {i + 1}º número: "))
        VET.append(num)
    return VET

def verificar_repetidos(VET):
    repetidos = {}
    
    for i, num in enumerate(VET):
        if num in repetidos:
            repetidos[num].append(i)
        else:
            repetidos[num] = [i]
    
    for num, posicoes in repetidos.items():
        if len(posicoes) > 1:
            print(f"O número {num} está repetido nas posições: {posicoes}")

def main():
    VET = ler_numeros()
    verificar_repetidos(VET)

if __name__ == "__main__":
    main()