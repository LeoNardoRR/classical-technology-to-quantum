from qiskit import QuantumCircuit, transpile, assemble
from qiskit.providers.aer import AerSimulator
from qiskit.algorithms import Shor

# Defina o número a ser fatorado
N = 21

# Crie um circuito quântico para o algoritmo de Shor
shor = Shor(N)

# Obtenha o circuito quântico para o algoritmo de Shor
circuit = shor.construct_circuit()

# Transpile o circuito para o simulador Aer
simulator = AerSimulator()
tqc = transpile(circuit, simulator)

# Execute o circuito no simulador
result = simulator.run(tqc).result()

# Obtenha a estimativa do fator primo
factors = shor.factor(result)
print(f"Fatores primos de {N}: {factors.factors}")
