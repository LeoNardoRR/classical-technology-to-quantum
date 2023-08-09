from qsharp import Result
from Microsoft.Quantum.Samples import ShorAlgorithm

# Executa o algoritmo de Shor
result = ShorAlgorithm.simulate()

# Mostra o resultado retornado do algoritmo
print(result)
