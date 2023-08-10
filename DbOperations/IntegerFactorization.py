import time
import qsharp
from IntegerFactorization import FactorInteger

num = int(input("Digite um número inteiro para fatorar: "))

start_time = time.time()
factors = FactorInteger.simulate(N=num)
end_time = time.time()

print(f"Fatores de {num}: {factors}")
print(f"Tempo de execução: {end_time - start_time:.6f} segundos")
