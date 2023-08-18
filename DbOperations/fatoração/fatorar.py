import random
from sympy import isprime
import time

def generate_prime(digits):
    while True:
        num = random.randint(10 ** (digits - 1), 10 ** digits - 1)
        if isprime(num):
            return num

def factorize(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

prime = generate_prime(5)  # Gera um número primo com 10 dígitos
print('Número primo gerado:', prime)
print('Fatorando...aguarde!')

start_time = time.time()
factors = factorize(prime)
end_time = time.time()

print(f"Fatores de {prime}: {factors}")
print(f"Tempo de execução: {end_time - start_time:.6f} segundos")
