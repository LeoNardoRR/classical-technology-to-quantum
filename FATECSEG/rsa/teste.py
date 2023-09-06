from qiskit import QuantumCircuit, transpile, assemble
from qiskit.visualization import plot_bloch_multivector
from qiskit.providers.aer import AerSimulator

# Crie um circuito quântico com um qubit
qc = QuantumCircuit(1)

# Simule o estado do qubit usando um simulador
simulator = AerSimulator()
job = assemble(transpile(qc, simulator))
result = simulator.run(job).result()
statevector = result.get_statevector()

# Exiba o estado do qubit em um gráfico de bloch
plot_bloch_multivector(statevector)
