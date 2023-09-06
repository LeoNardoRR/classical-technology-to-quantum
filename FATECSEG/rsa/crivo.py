import math
import time
import secrets

num_bytes = 256 // 8
chave_hexadecimal = secrets.token_hex(num_bytes)

print(f"Chave de 256 bits (hexadecimal): {chave_hexadecimal}")

chave_numero = int(chave_hexadecimal, 16)

print(f"Chave de 256 bits (decimal): {chave_numero}")

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
print("Fatorando!")
numero_para_fatorar = chave_numero

inicio = time.time()
fatores_primos = fatoracao_quadratica(numero_para_fatorar)
fim = time.time()

tempo_decorrido = fim - inicio

print(f"Os fatores primos de {numero_para_fatorar} são: {fatores_primos}")
print(f"Tempo decorrido: {tempo_decorrido} segundos")
