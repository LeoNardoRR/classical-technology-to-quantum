import math
import random
from fractions import Fraction
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute, Aer

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def shor_algorithm(N):
    # Passo 1: Escolher um número aleatório 'a' menor que N
    a = random.randint(2, N - 1)

    # Passo 2: Calcular o MDC entre 'a' e N
    mdc = gcd(a, N)
    if mdc > 1:
        # O MDC indica um fator não trivial de N
        return [mdc]

    # Passo 3: Preparação do algoritmo quântico
    period_found = False
    r = 0
    while not period_found:
        r += 1
        # Passo 3.1: Preparar o estado quântico inicial
        qreg = QuantumRegister(math.ceil(math.log2(N)), 'q')
        creg = ClassicalRegister(math.ceil(math.log2(N)), 'c')
        circuit = QuantumCircuit(qreg, creg)

        circuit.h(qreg)  # Aplicar a porta Hadamard a todos os qubits

        # Passo 3.2: Aplicar a exponenciação modular controlada
        for power in range(r):
            circuit.x(qreg[power])
            for i in range(2 ** power):
                circuit.swap(qreg[i], qreg[i + power + 1])
            circuit.x(qreg[power])

        # Passo 3.3: Aplicar a transformada de Fourier quântica
        circuit.append(qft(qreg, inverse=True), qreg)

        # Passo 3.4: Medir o resultado
        circuit.measure(qreg, creg)

        # Passo 4: Executar o circuito quântico
        backend = Aer.get_backend('qasm_simulator')
        job = execute(circuit, backend, shots=1)

        # Passo 5: Analisar o resultado
        result = job.result()
        counts = result.get_counts(circuit)
        measured_periods = [int(k, 2) for k in counts.keys()]

        for measured_period in measured_periods:
            # Passo 5.1: Encontrar a fração contínua do período medido
            numerator, denominator = rationalize(measured_period / (2 ** r), N)
            if numerator != 0 and denominator != 0:
                # Passo 5.2: Verificar se a fração contínua é válida
                if (a ** denominator) % N == 1:
                    period_found = True
                    break

    # Passo 6: Calcular os fatores usando a fração contínua
    factor1 = gcd(a ** (denominator // 2) + 1, N)
    factor2 = gcd(a ** (denominator // 2) - 1, N)

    return [factor1, factor2]

# Função auxiliar para calcular a fração contínua

def rationalize(x, N):
    fractions = []
    while len(fractions) < 1000:  # Limita o número de iterações para evitar loops infinitos
        fraction = Fraction(x).limit_denominator(N)
        numerator, denominator = fraction.numerator, fraction.denominator

        if denominator > 1:
            fractions.append((numerator, denominator))
            x = denominator / (N % denominator)
        else:
            break

    # Retorna a fração com o menor denominador encontrado
    min_denominator = float('inf')
    best_fraction = None
    for numerator, denominator in fractions:
        if denominator < min_denominator:
            min_denominator = denominator
            best_fraction = (numerator, denominator)

    return best_fraction