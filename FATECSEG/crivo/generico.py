import math
import time

def fatoracao_em_primos(numero):
    fatores_primos = []
    divisor = 2

    while divisor * divisor <= numero:
        if numero % divisor == 0:
            fatores_primos.append(divisor)
            numero //= divisor
        else:
            divisor += 1

    if numero > 1:
        fatores_primos.append(numero)

    return fatores_primos

# Solicite ao usuário que insira um número para realizar a fatoração em primos
numero_para_fatorar = int(input("Digite um número para fatorar em primos: "))

# Medir o tempo de execução
inicio = time.time()
fatores_primos = fatoracao_em_primos(numero_para_fatorar)
fim = time.time()

tempo_decorrido = fim - inicio

print(f"Os fatores primos de {numero_para_fatorar} são: {fatores_primos}")
print(f"Tempo decorrido para fatoração: {tempo_decorrido} segundos")
