import qsharp
qsharp.packages.add("Microsoft.Quantum.Standard")

from Microsoft.Quantum.Samples import ShorAlgorithm

N = 15  # O número que deseja fatorar
result = ShorAlgorithm.simulate(N)

if result != N:
    factor = result.value
    print("Fator encontrado:", factor)
else:
    print("Fator não encontrado.")
