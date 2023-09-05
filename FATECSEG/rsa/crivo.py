import math
import time

def calcular_mdc(a, b):
    while b:
        a, b = b, a % b
    return a

def fatoracao_quadratica(numero):
    if numero < 2:
        return [numero]

    fatores_primos = []
    while numero % 2 == 0:
        fatores_primos.append(2)
        numero //= 2

    if numero == 1:
        return fatores_primos

    for a in range(3, int(math.sqrt(numero)) + 1, 2):
        while numero % a == 0:
            fatores_primos.append(a)
            numero //= a

    if numero > 1:
        fatores_primos.append(numero)

    return fatores_primos

# Solicite ao usuário que insira um número para realizar a fatoração em primos
numero_para_fatorar = int(input("Digite um número para fatorar em primos: "))

# Medir o tempo de execução
inicio = time.time()
fatores_primos = fatoracao_quadratica(numero_para_fatorar)
fim = time.time()

tempo_decorrido = fim - inicio

print(f"Os fatores primos de {numero_para_fatorar} são: {fatores_primos}")
print(f"Tempo decorrido: {tempo_decorrido} segundos")
