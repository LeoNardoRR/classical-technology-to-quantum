import random
import time

def generate_even(digits):
    while True:
        num = random.randint(10 ** (digits - 1), 10 ** digits - 1)
        if num % 2 == 0:  # Verifica se o número gerado é par
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

num_even = generate_even(10)  # Gera um número par com 10 dígitos
print('Número par gerado:', num_even)
print('Fatorando...aguarde!')

start_time = time.time()
factors = factorize(num_even)
end_time = time.time()

print(f"Fatores de {num_even}: {factors}")
print(f"Tempo de execução: {end_time - start_time:.6f} segundos")
