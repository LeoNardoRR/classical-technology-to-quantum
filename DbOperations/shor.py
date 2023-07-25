import qsharp

# Importa a operação Q#
from ClassicalToQuantum import FactorizeNumber

# Número a ser fatorado
number_to_factorize = 21

# Chama a operação Q# para fatorar o número
factors = FactorizeNumber.simulate(N=number_to_factorize)

print(f"Os fatores primos de {number_to_factorize} são: {factors}")
